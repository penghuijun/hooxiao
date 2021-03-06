#include "fsm_business_state.h"
#include "global_var.h"


    /*******************************************************************************************************/
    /*					                       FsmBusinessState						       					   */
    /*******************************************************************************************************/
    IMPL_LOGGER(FsmBusinessState, logger);

#define IMPL_FSM_STATE(classname, name) classname FsmBusinessState::name(#classname)
    IMPL_FSM_STATE(FsmBusinessStateInit, state_init);
    IMPL_FSM_STATE(FsmBusinessStateWaitThread, state_wait_thread);
    IMPL_FSM_STATE(FsmBusinessStateEnd, state_end);
#undef IMPL_FSM_STATE

    void FsmBusinessState::enter(FsmBusiness& fsm)
    {

    }
    void FsmBusinessState::exit(FsmBusiness& fsm)
    {

    }

    void FsmBusinessState::client_req_event(FsmBusiness& fsm, lce::net::ConnectionInfo& conn, const hoosho::msg::Msg& stMsg)
    {
    	LOG4CPLUS_DEBUG(logger, "default client_req_event, state: "<<this->name());
    }
	void FsmBusinessState::thread_reply_event(FsmBusiness& fsm, ExecutorThreadResponseElement& element)
	{
		LOG4CPLUS_DEBUG(logger, "default thread_reply_event, state: "<<this->name());
	}
    void FsmBusinessState::timeout_event(FsmBusiness& fsm, void* param)
    {
    	LOG4CPLUS_DEBUG(logger, "default timeout_event, state: "<<this->name());
    }

	
    /*******************************************************************************************************/
    /*                                                                                  FsmBusinessStateInit                                                                                         */
    /*******************************************************************************************************/
    void FsmBusinessStateInit::client_req_event(FsmBusiness& fsm, lce::net::ConnectionInfo& conn, const hoosho::msg::Msg& stMsg)
    {
        //save async req param to fsm
        fsm._conn_id = conn.get_id();
        fsm._msg.CopyFrom(stMsg);

		if(::hoosho::msg::J_USER_LOGIN_REQ == fsm._msg.head().cmd())
		{
			ExecutorThreadRequestElement stThreadRequest(ExecutorThreadRequestType::T_USER_LOGIN
													, FsmContainer<int>::FSM_TYPE_BUSINESS
													, fsm._id);
			stThreadRequest.need_reply();
			stThreadRequest.m_snsapi_base_pre_auth_code = fsm._msg.user_login_req().pre_auth_code();
			g_executor_thread_processor->send_request(stThreadRequest);
		}
		else if(::hoosho::msg::J_GET_USER_INFO_REQ == fsm._msg.head().cmd())
		{
			ExecutorThreadRequestElement stThreadRequest(ExecutorThreadRequestType::T_USERINFO_QUERY
													, FsmContainer<int>::FSM_TYPE_BUSINESS
													, fsm._id);
			stThreadRequest.need_reply();
			for(int i=0; i!=fsm._msg.get_user_info_req().openid_list_size(); ++i)
			{
				stThreadRequest.m_openid_list.push_back(fsm._msg.get_user_info_req().openid_list(i));
			}
			g_executor_thread_processor->send_request(stThreadRequest);
		}
		else if(::hoosho::msg::J_UPDATE_USER_INFO_REQ == fsm._msg.head().cmd())
		{
			ExecutorThreadRequestElement stThreadRequest(ExecutorThreadRequestType::T_USERINFO_UPDATE
													, FsmContainer<int>::FSM_TYPE_BUSINESS
													, fsm._id);
			stThreadRequest.need_reply();
			stThreadRequest.m_user_info.set_openid(fsm._msg.update_user_info_req().openid());
			stThreadRequest.m_user_info.set_self_desc(fsm._msg.update_user_info_req().self_desc());
			g_executor_thread_processor->send_request(stThreadRequest);
		}
		
        fsm.set_state(FsmBusinessState::state_wait_thread);
        return;		
    }

	/*******************************************************************************************************/
    /*                                                                                  FsmBusinessStateWaitThread                                                                  */
    /*******************************************************************************************************/
	void FsmBusinessStateWaitThread::enter(FsmBusiness& fsm)
    {
        fsm.reset_timer(g_server->config().get_int_param("FSM_CONTAINER", "timeout"));
    }
    void FsmBusinessStateWaitThread::exit(FsmBusiness& fsm)
    {
        fsm.cancel_timer();
    }

    void FsmBusinessStateWaitThread::thread_reply_event(FsmBusiness& fsm, ExecutorThreadResponseElement& element)
    {
        //cancel timer first
        fsm.cancel_timer();
		if(element.m_result_code == ExecutorThreadRequestType::E_NOT_PA_FANS)
		{
			LOG4CPLUS_ERROR(logger, "FsmBusinessStateWaitThread::thread_reply_event failed"
                        <<", fsmid:"<<fsm._id
                        <<", thread result="<<element.m_result_code);
                        
			fsm.reply_fail(::hoosho::msg::E_NOT_PA_FANS);
			return;
		}

		if(element.m_result_code != ExecutorThreadRequestType::E_OK)
		{
			LOG4CPLUS_ERROR(logger, "FsmBusinessStateWaitThread::thread_reply_event failed"
                        <<", fsmid:"<<fsm._id
                        <<", thread result="<<element.m_result_code);
                        
			fsm.reply_fail(::hoosho::msg::E_SERVER_INNER_ERROR);
			return;
		}

		hoosho::msg::Msg stRespMsg;
	    hoosho::msg::MsgHead* header = stRespMsg.mutable_head();
	    header->set_result(::hoosho::msg::E_OK);
	    header->set_seq(fsm._msg.head().seq());
		if(::hoosho::msg::J_GET_USER_INFO_REQ == fsm._msg.head().cmd())
		{
			header->set_cmd(::hoosho::msg::J_GET_USER_INFO_RES);
			::hoosho::j::user::GetUserInfoRes* pGetUserInfoRes = stRespMsg.mutable_get_user_info_res();
			for(size_t i=0; i!=element.m_user_info_list.size(); ++i)
			{
				pGetUserInfoRes->add_userinfo_list()->CopyFrom(element.m_user_info_list[i]);
			}
		}
		else if(::hoosho::msg::J_UPDATE_USER_INFO_REQ == fsm._msg.head().cmd())
		{
			header->set_cmd(::hoosho::msg::J_UPDATE_USER_INFO_RES);
		}
		else if(::hoosho::msg::J_USER_LOGIN_REQ == fsm._msg.head().cmd())
		{
			header->set_cmd(::hoosho::msg::J_USER_LOGIN_RES);
			
			::hoosho::j::user::UserLoginRes* pUserLoginRes = stRespMsg.mutable_user_login_res();
			pUserLoginRes->mutable_userinfo()->CopyFrom(element.m_user_info);

			//add login session
			ClientProcessor::LoginSessionInfo stLoginSessionInfo;
			g_client_processor->add_login_session(element.m_user_info.openid(), stLoginSessionInfo);
			
			pUserLoginRes->set_cookie_key(stLoginSessionInfo._openid);
			pUserLoginRes->set_cookie_value(stLoginSessionInfo._session);
			pUserLoginRes->set_cookie_life(g_server->config().get_int_param("SESSION", "life", 0));
		}
		
		g_client_processor->send_datagram(fsm._conn_id, stRespMsg);
		fsm.set_state(state_end);
		return;
    }

    void FsmBusinessStateWaitThread::timeout_event(FsmBusiness& fsm, void* param)
    {
        LOG4CPLUS_ERROR(logger, "FsmBusinessStateWaitThread time_out."
                        <<" fsmid:"<<fsm._id
                        <<" connid:"<<fsm._conn_id);
		fsm.reply_fail(::hoosho::msg::E_SERVER_TIMEOUT);
        fsm.set_state(FsmBusinessState::state_end);
        return;
    } 
    /*******************************************************************************************************/
    /*                                                                                     FsmBusinessStateEnd                                                                                     */
    /*******************************************************************************************************/
    void FsmBusinessStateEnd::enter(FsmBusiness& fsm)
    {
        g_fsm_business_container->del_fsm(&fsm);
    }

