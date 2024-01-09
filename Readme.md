Email verifier task 

Example to verify 
post http://127.0.0.1:8000/verify_email/ 

email : wellyshadow1@gmail.com

Example returning all verified email 

get http://127.0.0.1:8000/get-all-email-result/

Example deleting some verified email 

delete http://127.0.0.1:8000/delete-email-result/1/

Example update emails 

put http://127.0.0.1:8000/update-email-result/1/

You must create .env file with your Api key before start 

#base_url = 'http://127.0.0.1:8000'

#client = EmailVerificationClient(base_url)


#verification_result = client.verify_email('wellyggff@gmail.com')
#print("Verification Result:", verification_result)

#create_result = client.create_email_result('wellyggff@gmail.com')
#print("Create Result:", create_result)

#get_result = client.get_email_result(2) 
#print("Get Result:", get_result)

#update_result = client.update_email_result(1, is_valid=False)
#print("Update Result:", update_result)

#delete_result = client.delete_email_result(2)
#print("Delete Result:", delete_result)

#all =client.get_all_email_result()
#print("Result:", all)
