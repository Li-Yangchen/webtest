*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
test_get_event_list
    ${payload}=    Create Dictionary    eid=1
    Create Session    event    http://127.0.0.1:8000/
    ${r}=    GET On Session    event    api/get_event_list/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}   message
    Should Be Equal    ${msg}    success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}

test_add_event
    Create Session    event    http://127.0.0.1:8000/api
    &{headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    &{payload}=    Create Dictionary    eid=1
    ${r}=    POST On Session    event    api/add_event/    data=${payload}    headers=${headers}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    parameter error
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10021)
    Should Be Equal    ${sta}    ${status}

test_user_sign_success
    Create Session    event    http://127.0.0.1:8000/
    &{headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    &{payload}=    Create Dictionary    eid=1
    ${r}=    POST On Session    event    api/user_sign/    data=${payload}    headers=${headers}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    parameter error
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10021)
    Should Be Equal    ${sta}    ${status}
