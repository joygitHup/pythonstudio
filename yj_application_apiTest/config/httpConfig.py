host='http://192.168.1.117/kw/'
headers = {
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) yunji/0.0.1 Chrome/76.0.3809.146 Electron/6.1.12 Safari/537.36',
}
#loginApi
wholeURl='admin/signin/'
data1={"username":"admin","password":"adminadmin"}
data2={"username":"admin","password":"admin"}
data3={"username":"Admin","password":"adminadmin"}
data4={"username":"admin","password":"123456"}
#rebuid_member_a_list

#upload_file
wu='api/resources/uploadsignature/'
data={"type":2,"extension":"png"}
#wholeURl_upload
wholeURl_upload='admin/procedures/6bb9f788-cb02-11ea-a2d1-38f9d355d676/extends/'
dataUploa={"procedure_id":"6bb9f788-cb02-11ea-a2d1-38f9d355d676","type":8,"values":[{"resource_key":"sa_procedure/2ef6c8fa-0d04-11eb-92d4-0242ac190005.png","name":"logo.33b66427.png"},{"resource_key":"sa_procedure/31b5f472-0f60-11eb-92d4-0242ac190005.png","name":"logo.33b66427.png"}]}
# upload_file_data
host1='http://192.168.1.117:9001/'
upload_file_data_url='inspection/sa_procedure/76d6a1d0-11b0-11eb-92d4-0242ac190005.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20201019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201019T021157Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=50754a75b673ece0a11b9b649c8b346a64bb4f4ffe9c38f050ed50353b0fc2a1'

# new_rebuited_worksheet
new_rebuited_data_url='inspection/sa_rail_work_sheet_remark/1c9aea2c-11bb-11eb-9511-0242ac190005.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20201019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201019T032810Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=4739fd6b96c853e8da208f4f65f9462ae4d39a327e75f70c07451c580a7f3d96'

# editor_userinfor
editor_userinfor_host='admin/users/f941f6d6-fd76-11ea-aaac-0242ac190005/'
editor_userinfor_data={"username":"fdca1ef55eadbfe2707aea9f36f6b15a","password":"","last_name":"","first_name":"手机二","mobile":"","id_number":"111111111111111111","bind_devices":[]}


#work_setting_add_meterail
add_meterail_host='admin/procedures/eba533a6-11be-11eb-b6ca-0242ac190005/extends/'
add_meterail_data={"procedure_id":"eba533a6-11be-11eb-b6ca-0242ac190005","type":0,
                   "values":["{\"name\":\"das\",\"unit\":\"adas\",\"count\":\"asda\",\"id\":\"1du6scrjcyy\"}",
                            {"name":"sdas","unit":"asd ","count":"asd a","id":"znr1hj8q9c"}
                                                                                            ]}