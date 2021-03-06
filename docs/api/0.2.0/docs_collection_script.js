const postmanData = {
	"info": {
		"_postman_id": "aa99fd32-7714-4656-b0bf-659bf63b0fa6",
		"name": "Techfesia2019",
		"description": "API for Techfesia.",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "User Auth",
			"item": [
				{
					"name": "User Auth modes",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/auth_modes",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"auth_modes"
							]
						},
						"description": "Tells which all auth modes are enabled for a user.\nTypically 2 modes will exist,\n<ul>\n\t<li>password (true or false)</li>\n\t<li>o-auth (as an array containing providers)</li>\n</ul>"
					},
					"response": [
						{
							"name": "User Auth modes",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/auth_modes",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"auth_modes"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"password\":true,\n\t\"o-auth\":[\n\t\t\t\"google\",\n\t\t\t\"github\",\n\t\t\t\"facebook\"\n\t\t]\n}"
						}
					]
				},
				{
					"name": "Create Password",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"password\":\"{{password}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"password",
								""
							]
						},
						"description": "creates a password for those users who are signed in via o-auth.\nWill throw 422 if user already has password based auth enabled."
					},
					"response": [
						{
							"name": "Create Password",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"password\":\"{{password}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"password",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"message\":\"new password created\"\n}"
						}
					]
				},
				{
					"name": "Change Password",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"oldPassword\":\"old_passord\",\n\t\"newPassword\":\"new_password\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"password",
								""
							]
						},
						"description": "Changes the password of the user.\nWill throw a 422 if user is logged in via o-auth or if old password is incorrect."
					},
					"response": []
				},
				{
					"name": "Reset Password",
					"request": {
						"method": "PATCH",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"resetToken\":\"sampled_reset_token\",\n\t\"newPassword\":\"password\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"password",
								""
							]
						},
						"description": "resets user password to a new password.\nUser must send a reset_token in payload that will most likely be emailed to him"
					},
					"response": [
						{
							"name": "Reset Password",
							"originalRequest": {
								"method": "PATCH",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"resetToken\":\"sampled_reset_token\",\n\t\"newPassword\":\"password\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"password",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"message\":\"Password reset successfully\"\n}"
						},
						{
							"name": "Reset Password (invalid token)",
							"originalRequest": {
								"method": "PATCH",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"resetToken\":\"sampled_reset_token\",\n\t\"newPassword\":\"password\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/password/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"password",
										""
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\":{\n\t\t\"resetToken\":\"token is invalid, expired or already used. Please get a new token\"\n\t}\n}"
						}
					]
				}
			]
		},
		{
			"name": "Users",
			"item": [
				{
					"name": "Get Users (Staff only)",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users?limit=10",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users"
							],
							"query": [
								{
									"key": "limit",
									"value": "10",
									"description": "limit the number of entries"
								},
								{
									"key": "",
									"value": "",
									"disabled": true
								}
							]
						},
						"description": "Get details of all the users.\nset <field>=<value> to filter based on that value ex: username=test\n\nset limit=x to show only x entries.\nThen set page=y to view page y.\nExample: if you set limit=3 and you want to view entry no. 7, then set page=3.\n\nIf you request for a page more than max no of pages, then expect the following response:\n\n400 Bad Request\n{\n\tmessage:\"This page does not exist\",\n\t\"pageSize\": 3,\n\t\"noOfPages\":5\n}\n"
					},
					"response": [
						{
							"name": "Get Users (Exceed Page Limit)",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{staff_access_token}}",
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users?limit=10&page=100",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users"
									],
									"query": [
										{
											"key": "limit",
											"value": "10",
											"description": "limit the number of entries"
										},
										{
											"key": "page",
											"value": "100"
										}
									]
								}
							},
							"status": "Bad Request",
							"code": 400,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"message\":\"This page does not exist\",\n\t\"pageSize\":10,\n\t\"noOfPages\":5\n}"
						},
						{
							"name": "Get Users",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{staff_access_token}}",
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users?limit=3&page=2",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users"
									],
									"query": [
										{
											"key": "limit",
											"value": "3",
											"description": "limit the number of entries"
										},
										{
											"key": "page",
											"value": "2",
											"description": "page no"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"currentPage\": 2,\n\t\"noOfPages\":5,\n\t\"users\":[\n\t\t{\n\t\t\t\"publicId\":\"sampleId1\",\n\t\t\t\"username\":\"{{username}}\",\n\t\t\t\"firstName\":\"Test\",\n\t\t\t\"lastName\":\"User\",\n\t\t\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\t\t\"phoneNumber\":\"+911234567890\",\n\t\t\t\"collegeName\":\"Test College 123\",\n\t\t\t\"profilePicture\":\"url_to_profile_pic\",\n\t\t\t\"dateJoined\":\"date_time_in_iso_format\",\n\t\t\t\"lastLogin\":\"date_time_in_iso_format\"\n\t\t},\n\t\t\n\t\t{\n\t\t\t\"publicId\":\"sampleId2\",\n\t\t\t\"username\":\"test_user_002\",\n\t\t\t\"firstName\":\"Test\",\n\t\t\t\"lastName\":\"User2\",\n\t\t\t\"email\":\"test_user_002@testers.techfesia.iiits.in\",\n\t\t\t\"phoneNumber\":\"+911234567890\",\n\t\t\t\"collegeName\":\"Test College 123\",\n\t\t\t\"profilePicture\":\"url_to_profile_pic\",\n\t\t\t\"dateJoined\":\"date_time_in_iso_format\",\n\t\t\t\"lastLogin\":\"date_time_in_iso_format\"\n\t\t},\n\t\t{\n\t\t\t\"publicId\":\"sampleId3\",\n\t\t\t\"username\":\"test_user_003\",\n\t\t\t\"firstName\":\"Test\",\n\t\t\t\"lastName\":\"User\",\n\t\t\t\"email\":\"test_user_003@testers.techfesia.iiits.in\",\n\t\t\t\"phoneNumber\":\"+911234567890\",\n\t\t\t\"collegeName\":\"Test College 123\",\n\t\t\t\"profilePicture\":\"url_to_profile_pic\",\n\t\t\t\"dateJoined\":\"date_time_in_iso_format\",\n\t\t\t\"lastLogin\":\"date_time_in_iso_format\"\n\t\t}\n\t]\n}"
						}
					]
				},
				{
					"name": "Get User details",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}"
							]
						},
						"description": "Get details of a perticular user. \nOnly the user herself or the staff/superuser can access this route"
					},
					"response": [
						{
							"name": "Get user details",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"publicId\":\"sampleId123\",\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\",\n\t\"dateJoined\":\"date_time_in_iso_format\",\n\t\"lastLogin\":\"date_time_in_iso_format\"\n\t\n}"
						}
					]
				},
				{
					"name": "Get User State (Staff Only)",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/privileges",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"privileges"
							]
						},
						"description": "Shows the state of a user.\nResponds with one of the following strings:\n<ul>\n\t<li>disabled</li>\n\t<li>normal</li>\n\t<li>staff</li>\n\t<li>superuser</li>\n<ul>\n\nIf the user is a staff, then also provides an array containing the permissions of the user on each model.\n\nNote that a disabled user can not do anything even if s(he) was a superuser."
					},
					"response": [
						{
							"name": "Get User State",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{staff_access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/privileges",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"privileges"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"state\":\"normal\"\n}"
						},
						{
							"name": "Get Staff User State",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{staff_access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{staff_username}}/privileges",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{staff_username}}",
										"privileges"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"state\":\"staff\",\n\t\"privileges\":{\n\t\t\"model_name\":[\"array\", \"of\", \"privileges\"],\n\t\t\"user\":[\"read\"],\n\t\t\"event\":[\"read\", \"create\", \"update\", \"delete\"],\n\t\t\"firebaseUser\":[]\n\t}\n}"
						},
						{
							"name": "Get SuperUser State (Staff Only)",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{staff_access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{superuser_username}}/privileges",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{superuser_username}}",
										"privileges"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"state\":\"superuser\"\n}"
						}
					]
				},
				{
					"name": "Create New User",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"password\":\"{{password}}\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								""
							]
						},
						"description": "Create a new User. \nMandatory fields are:\n<ul>\n\t<li>username</li>\n\t<li>email</li>\n\t<li>password</li>\n</ul>"
					},
					"response": [
						{
							"name": "Create New User",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"password\":\"{{password}}\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n    \"publicId\": \"sampleId123\",\n    \"username\": \"{{username}}\",\n    \"firstName\": \"Test\",\n    \"lastName\": \"User\",\n    \"email\": \"{{username}}@testers.techfesia.iiits.in\",\n    \"phoneNumber\": \"+911234567890\",\n    \"collegeName\": \"Test College 123\",\n    \"profilePicture\": \"url_to_profile_pic\",\n    \"dateJoined\": \"date_time_in_iso_format\",\n    \"lastLogin\": \"date_time_in_iso_format\"\n}"
						},
						{
							"name": "Create New User (Missing Required field)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"password\":\"{{password}}\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										""
									]
								}
							},
							"status": "Bad Request",
							"code": 400,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"errors\":{\n\t\t\"username\":\"missing required field\"\n\t}\n}"
						},
						{
							"name": "Create New User (Username Exists)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"password\":\"{{password}}\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										""
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"errors\":{\n\t\t\t\"username\":\"This username already exists\"\n\t}\n}"
						}
					]
				},
				{
					"name": "Update User Details",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}?=",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}"
							],
							"query": [
								{
									"key": "",
									"value": ""
								}
							]
						},
						"description": "updates a user's details.\nDo note that some fields might be immutable in which case a 422 will be returned\nAlso can not be used for updating password."
					},
					"response": [
						{
							"name": "Update User Details",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{access_token}}"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"firstName\":\"Test\",\n\t\"lastName\":\"User\",\n\t\"email\":\"{{username}}@testers.techfesia.iiits.in\",\n\t\"phoneNumber\":\"+911234567890\",\n\t\"collegeName\":\"Test College 123\",\n\t\"profilePicture\":\"url_to_profile_pic\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}?=",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}"
									],
									"query": [
										{
											"key": "",
											"value": ""
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"publicId\":\"sampleId123\",\n    \"username\": \"{{username}}\",\n    \"firstName\": \"Test\",\n    \"lastName\": \"User\",\n    \"email\": \"{{username}}@testers.techfesia.iiits.in\",\n    \"phoneNumber\": \"+911234567890\",\n    \"collegeName\": \"Test College 123\",\n    \"profilePicture\": \"url_to_profile_pic\"\n}"
						}
					]
				},
				{
					"name": "Update profile picture (O-Auth)",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"provider\":\"google\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/picture",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"picture"
							]
						},
						"description": "Updates the user's profile picture from o-auth provider like google/github\nName of o-auth provider should be specified in the payload. If not specified, take the first default provider available.\n\nThrows 422 if o-auth is not enabled."
					},
					"response": [
						{
							"name": "Update profile picture using O-Auth",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"provider\":\"google\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/picture",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"picture"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"message\":\"Profile Picture updated\"\n}"
						}
					]
				},
				{
					"name": "Disable User (Staff Only)",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/disable",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"disable"
							]
						},
						"description": "disables a user account, preventing him/her from logging in or perform any action"
					},
					"response": []
				},
				{
					"name": "Delete User (Staff Only)",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								""
							]
						},
						"description": "Delete a user account. \n<b><i>\n<span style=\"color:red\">\nWarning: There is no way to recover data once this request is sent. Consider disabling the account instead.\n</span>\n</b></i>"
					},
					"response": [
						{
							"name": "Delete User (Staff Only)",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": null,
							"header": null,
							"cookie": [],
							"body": null
						}
					]
				},
				{
					"name": "Update Profile Photo",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"value": "multipart/form-data",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "picture",
									"type": "file",
									"src": []
								}
							]
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/pictureupload",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"pictureupload"
							]
						},
						"description": "Update profile picyure by uploading a photo."
					},
					"response": [
						{
							"name": "Update Profile Photo by sending wrong file",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "multipart/form-data",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "picture",
											"type": "file",
											"src": "/home/ram/.local/lib/python3.6/site-packages/tensorflow/python/__init__.py"
										}
									]
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/pictureupload",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"pictureupload"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Only image type data allowed\"\n}"
						},
						{
							"name": "Update Profile Picture by uploading pic",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "multipart/form-data",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "picture",
											"type": "file",
											"src": "/home/ram/Pictures/MyPic.jpg"
										}
									]
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/pictureupload",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"pictureupload"
									]
								}
							},
							"status": "Accepted",
							"code": 202,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"message\": \"Profile Picture Updated\"\n}"
						}
					]
				}
			]
		},
		{
			"name": "Authentication",
			"item": [
				{
					"name": "User Token Pair Obtain",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"password\":\"{{password}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								""
							]
						},
						"description": "Submit username and password, get accessToken and refreshToken in return."
					},
					"response": [
						{
							"name": "User Token Pair Obtain",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{username}}\",\n\t\"password\":\"{{password}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/obtain/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"obtain",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n  \"access\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU\",\n  \"refresh\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4\"\n}"
						}
					]
				},
				{
					"name": "User Token Refresh",
					"event": [
						{
							"listen": "test",
							"script": {
								"id": "49d5c21b-8879-4cbf-8299-d84a8d5c7f4e",
								"exec": [
									""
								],
								"type": "text/javascript"
							}
						}
					],
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"refresh\":\"{{refresh_token}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								"refresh",
								""
							]
						},
						"description": "Submit refreshToken and get back another accessToken"
					},
					"response": [
						{
							"name": "User Token Refresh",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"refresh\":\"{{refresh_token}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"refresh",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w\"\n}"
						}
					]
				},
				{
					"name": "Staff token pair obtain",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\":\"{{staff_username}}\",\n\t\"password\":\"{{staff_password}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								""
							]
						},
						"description": "Same as user_token_pair_obtain\n<b>Staff Only</b>"
					},
					"response": [
						{
							"name": "Staff token pair obtain",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{staff_username}}\",\n\t\"password\":\"{{staff_password}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/obtain/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"obtain",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU\",\n    \"refresh\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4\"\n}"
						}
					]
				},
				{
					"name": "Staff Token Refresh",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"refresh\":\"{{staff_refresh_token}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								"refresh",
								""
							]
						},
						"description": "Same as user_token_refresh\n<b>Staff Only</b>"
					},
					"response": [
						{
							"name": "Staff Token Refresh",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"refresh\":\"{{staff_refresh_token}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"refresh",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w\"\n}"
						}
					]
				},
				{
					"name": "SuperUser Token Pair obtain",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\":\"{{superuser_username}}\",\n\t\"password\":\"{{superuser_password}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								""
							]
						},
						"description": "Same as user_token_pair_obtain\n<b>Superuser Only</b>"
					},
					"response": [
						{
							"name": "SuperUser Token Pair obtain",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\":\"{{superuser_username}}\",\n\t\"password\":\"{{superuser_password}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/obtain/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"obtain",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n  \"access\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU\",\n  \"refresh\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4\"\n}"
						}
					]
				},
				{
					"name": "SuperUser Token Refresh",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"refresh\":\"{{superuser_refresh_token}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								"refresh",
								""
							]
						},
						"description": "Same as user_token_pair_obtain\n<b>Superuser Only</b>"
					},
					"response": [
						{
							"name": "SuperUser Token Refresh",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text",
										"disabled": true
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"refresh\":\"{{superuser_refresh_token}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/refresh/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										"refresh",
										""
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"access\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w\"\n}"
						}
					]
				},
				{
					"name": "Revoke All Tokens (Sign Out from all devices)",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								""
							]
						},
						"description": "Revokes the given refresh tokens signing out the user from perticular device.\n\nIf no token is provided in body, then all tokens related to user are deleted, signing out the user from everywhere."
					},
					"response": [
						{
							"name": "Revoke All Tokens (Sign out from Some Devices)",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"tokens_deleted\":5\n}"
						}
					]
				},
				{
					"name": "Revoke one token (Signout from one device)",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"token\":\"{{refresh_token}}\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/auth/token/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"auth",
								"token",
								""
							]
						},
						"description": "Revokes a single refresh token. i.e. signs out the user from a perticular device. \nA PUT method instead of DELETE is used here as DELETE doesn't support payloads."
					},
					"response": [
						{
							"name": "Revoke one token (Signout from one device)",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"token\":\"{{refresh_token}}\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/auth/token/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"auth",
										"token",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Content-Type",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n\t\"tokens_deleted\":1\n}"
						}
					]
				}
			],
			"auth": {
				"type": "noauth"
			},
			"event": [
				{
					"listen": "prerequest",
					"script": {
						"id": "382510a1-077a-463a-926f-8233fdacdb68",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				},
				{
					"listen": "test",
					"script": {
						"id": "a88c4c32-4eee-4756-90d2-422c55b1b410",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				}
			]
		},
		{
			"name": "Category",
			"item": [
				{
					"name": "Get list of categories",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/category",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"category"
							]
						},
						"description": "Get list of all the categories. No option like limit or sort allowed. Categories identify kind of events. Each event is necessarily associated with one or more categories."
					},
					"response": [
						{
							"name": "Get list of all the existing categories.",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"name\": \"Hackathon\",\n\t\t\"description\": \"This events are contests to test your innovation and speed.\"\n\t},\n\t{\n\t\t\"name\": \"Coding Event\",\n\t\t\"description\": \"Code, Code and code.\"\n\t}\n]"
						}
					]
				},
				{
					"name": "Add a new Category",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"name\": \"Name of Category\",\n\t\"description\": \"Description about the Category (Optional)\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/category",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"category"
							]
						},
						"description": "Creating new Category. Each category is uniquely identified by its name. Descriptions are optional. Only Staff can make new categories. A category named 'Others' exists by default."
					},
					"response": [
						{
							"name": "Creating a new category",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"name\": \"Hackathon\",\n\t\"description\": \"Contest for testing your problem solving skills.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category"
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"name\": \"Hackathon\",\n\t\"description\": \"Contest for testing your problem solving skills.\"\n}"
						},
						{
							"name": "Trying to create existing category",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"name\": \"Others\",\n\t\"description\": \"This category exists by default.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category?",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category"
									],
									"query": [
										{
											"key": "",
											"value": "",
											"disabled": true
										}
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"This category already exist.\"\n}"
						}
					]
				},
				{
					"name": "Edit a Category Description",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"description\": \"Update the description for this category.\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/tags/{{category_name}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"tags",
								"{{category_name}}"
							]
						},
						"description": "Allow editing description for a category. Staff Only."
					},
					"response": [
						{
							"name": "Update Description",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"description\": \"Very difficult to win prizes in it.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category/Hackathon",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category",
										"Hackathon"
									]
								}
							},
							"status": "Accepted",
							"code": 202,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"name\": \"Hackathon\",\n    \"description\": \"Very difficult to win prizes in it.\"\n}"
						},
						{
							"name": "Updating a non existing Category",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"description\": \"This category does not exist.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category/InvalidCategory",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category",
										"InvalidCategory"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Category does not exist.\"\n}"
						}
					]
				},
				{
					"name": "Delete a Category",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
									"type": "string"
								}
							]
						},
						"method": "DELETE",
						"header": [
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/category/{{category_name}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"category",
								"{{category_name}}"
							]
						},
						"description": "Delete Tags. Can only delete an existing tag if no event is using it. Staff Only."
					},
					"response": [
						{
							"name": "Deleting a category that is created but not used",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category/Hackathon",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category",
										"Hackathon"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "Text",
							"header": [],
							"cookie": [],
							"body": ""
						},
						{
							"name": "Deleting a non-existing Category",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category/InvalidCategory",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category",
										"InvalidCategory"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"This category does not exixt.\"\n}"
						},
						{
							"name": "Deleting a category that is being used",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/category/Coding?",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"category",
										"Coding"
									],
									"query": [
										{
											"key": "",
											"value": "",
											"disabled": true
										}
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Cant delete a category that is in use.\"\n}"
						}
					]
				}
			],
			"description": "Category: Every event is associated with a category. For Example: Hackathon, Workshop, Coding, Designing, Exhibition."
		},
		{
			"name": "Tags",
			"item": [
				{
					"name": "Get list of Tags",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/tags",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"tags"
							]
						},
						"description": "Get list of all the tags. No option like limit or sort allowed. Tags are optional. They are used for highlighting something about the event."
					},
					"response": [
						{
							"name": "Get list of all the existing Tags",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"name\": \"Begineer\",\n\t\t\"description\": \"Good for begineers.\"\n\t},\n\t{\n\t\t\"name\": \"Free\",\n\t\t\"description\": \"This event is free.\"\n\t}\n]"
						}
					]
				},
				{
					"name": "Add a new Tag",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"name\": \"Name of Tag\",\n\t\"description\": \"Description about use of Tag (Optional)\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/tags",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"tags"
							]
						},
						"description": "Creating new Tags. Each tag is uniquely identified by its name. Can add an optional description. Only Staff can add new Tags."
					},
					"response": [
						{
							"name": "Trying to create existing tag",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"name\": \"Begineer\",\n\t\"description\": \"Trying to create same tag again!\"\n}"
								},
								"url": {
									"raw": "/events/tags?",
									"path": [
										"events",
										"tags"
									],
									"query": [
										{
											"key": "",
											"value": "",
											"disabled": true
										}
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Tag already exist.\"\n}"
						},
						{
							"name": "Creating a new tag",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"name\": \"Begineer\",\n\t\"description\": \"Event is good for begineers.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags"
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"name\": \"Begineer\",\n\t\"description\": \"Event is good for begineers.\"\n}"
						}
					]
				},
				{
					"name": "Edit a tag description",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"description\": \"Update the description for this tag.\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/tags/{{tags_name}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"tags",
								"{{tags_name}}"
							]
						},
						"description": "Allow editing description for a tag. Staff Only."
					},
					"response": [
						{
							"name": "Update Description",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"description\": \"Good for begineers but no prizes in this event.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags/Begineer",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags",
										"Begineer"
									]
								}
							},
							"status": "Accepted",
							"code": 202,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"name\": \"Begineer\",\n    \"description\": \"Good for begineers but no prizes in this event.\"\n}"
						},
						{
							"name": "Updating a non existing Tag",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"description\": \"This tag does not exist.\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags/InvalidTag",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags",
										"InvalidTag"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Tag does not exist.\"\n}"
						}
					]
				},
				{
					"name": "Delete a Tag",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "DELETE",
						"header": [
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/tags/{{tags_name}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"tags",
								"{{tags_name}}"
							]
						},
						"description": "Delete Tags. Can only delete an existing tag if no event is using it. Staff Only."
					},
					"response": [
						{
							"name": "Deleting a tag that is created but not used",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags/Begineer",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags",
										"Begineer"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "Text",
							"header": [],
							"cookie": [],
							"body": ""
						},
						{
							"name": "Deleting a tag that is being used",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags/InUseTag?",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags",
										"InUseTag"
									],
									"query": [
										{
											"key": "",
											"value": "",
											"disabled": true
										}
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Cant delete a tag that is in use.\"\n}"
						},
						{
							"name": "Deleting a non-existing Tag",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/tags/InvalidTag",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"tags",
										"InvalidTag"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"This tag does not exixt.\"\n}"
						}
					]
				}
			],
			"description": "Tags: A small highlight about a event. For Example: Free, Difficult, Special. It is optional. "
		},
		{
			"name": "Events",
			"item": [
				{
					"name": "Get list of events",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events?limit&page&category&order&tags",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events"
							],
							"query": [
								{
									"key": "limit",
									"value": null,
									"description": "Set limit of events returned"
								},
								{
									"key": "page",
									"value": null,
									"description": "Set page number of returned event"
								},
								{
									"key": "category",
									"value": null,
									"description": "Search in specific categories(can be multiple values)"
								},
								{
									"key": "order",
									"value": null,
									"description": "Orders returned event by date or name"
								},
								{
									"key": "tags",
									"value": null,
									"description": "Search for events with specified tags(can be multiple values)"
								}
							]
						},
						"description": "Get list of events. Can be accessed by anyone.\n\nWould return only id, name, description, date, time, venue, category and tags for a event."
					},
					"response": [
						{
							"name": "Get an event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{access_token}}",
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events?category=Coding&category=Hackathon&order=date&tags=Begineer",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events"
									],
									"query": [
										{
											"key": "category",
											"value": "Coding",
											"description": "Search in specific categories"
										},
										{
											"key": "category",
											"value": "Hackathon"
										},
										{
											"key": "order",
											"value": "date",
											"description": "Orders returned event by date or name"
										},
										{
											"key": "tags",
											"value": "Begineer"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"events\": [\n        {\n            \"publicId\": \"1\",\n            \"eventPicture\":\"some url\",\n            \"eventLogo\":\"some url\",\n            \"name\": \"Codechef Elektra\",\n            \"description\": \"A 3 hour long competitive coding contest which tests your problem solving and coding skills.\",\n            \"date\": \"2019-09-24\",\n            \"time\": \"09:30\",\n            \"venue\": \"Computer Lab\",\n            \"category\": [\n                \"Coding\",\n                \"Contest\"\n            ],\n            \"tags\": [\n                \"Prime Event\",\n                \"Special Prizes\"\n            ]\n        },\n        {\n            \"publicId\": \"2\",\n            \"name\": \"Reverse Coding\",\n            \"description\": \"Find questions from answer by solving riddles.\",\n            \"date\": \"2019-09-21\",\n            \"time\": \"17:30\",\n            \"venue\": \"Computer Lab\",\n            \"category\": [\n                \"Coding\",\n                \"Hackathon\"\n            ],\n            \"tags\": [\n                \"Begineer\",\n                \"Special Prizes\"\n            ]\n        }\n    ]\n}"
						}
					]
				},
				{
					"name": "Create a new Event",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}",
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman."
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\": \"Name of the Event\",\n    \"description\": \"Event Description\",\n    \"date\": \"YYYY-MM-DD\",\n    \"time\": \"HH:MM\",\n    \"venue\": \"Event Venue\",\n    \"fees\": \"Participation Fee\",\n    \"prize\": [\"First Prize\", \"Second Prize\", \"Prize for innovation\"],\n    \"teamEvent\": true,\n    \"minSize\": 3,\n    \"maxSize\": 8,\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Question with multiple Answers\",\n            \"Answer\"\n        ],\n        [\n            \"Put Question 2\",\n            \"Put Answer here\"\n        ]\n    ],\n    \"category\": [\n        \"Defaults to Others\",\n        \"Can be an array of valid categories\"\n    ],\n    \"tags\": [\n        \"Optional\",\n        \"Can be an array of valid tags\"\n    ]\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events"
							]
						},
						"description": "Add a new Event. Staff can only add event\n\nName: Name of the Event\n\nDescription: Event Description\n\nDate: Event Day\n\nTime: Start Time\n\nVenue: Event Venue\n\nFees: Participation Fee\n\nPrize: Prize for event in Array\n\nTeam Event: Is the event for team or individual\n\nMin Size: Minimum number of members(Required if Team Event)\n\nMax Size: Maximum number of members(Required if Team Event)\n\nContact No: Array of phone numbers\n\n**Optional:**\n\nRules: Array of Rules\n\nFAQ: Array of FAQs in [Question, Answer] format\n\nCategory: Array of category for this event. If left blank would default to [Others]\n\nTags: Array of Tags.\n"
					},
					"response": [
						{
							"name": "Adding a new Event",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"Codechef Elektra\",\n    \"description\": \"A 3 hour long competitive coding contest which tests your problem solving and coding skills.\",\n    \"date\": \"2019-09-24\",\n    \"time\": \"09:30\",\n    \"venue\": \"Computer Lab\",\n    \"fees\": \"Rs 300\",\n    \"prize\": [\"First Prize: 2000\", \"Second Prize: 1500\", \"Third Prize: 1000\", \"100 Ladoos to top 15 coders\"],\n    \"teamEvent\": true,\n    \"minSize\": 3,\n    \"maxSize\": 8,\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Why laptop is required?\",\n            \"To code\"\n        ],\n        [\n            \"What are pre-requirements\",\n            \"Have an Hackerrank ID\"\n        ]\n    ],\n    \"category\": [\n        \"Coding\",\n        \"Contest\"\n    ],\n    \"tags\": [\n        \"Prime Event\",\n        \"Special Prizes\"\n    ]\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events"
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"name\": \"Codechef Elektra\",\n    \"description\": \"A 3 hour long competitive coding contest which tests your problem solving and coding skills.\",\n    \"date\": \"2019-09-24\",\n    \"time\": \"09:30\",\n    \"venue\": \"Computer Lab\",\n    \"fees\": \"Rs 300\",\n    \"prize\": [\n        \"First Prize: 2000\",\n        \"Second Prize: 1500\",\n        \"Third Prize: 1000\",\n        \"100 Ladoos to top 15 coders\"\n    ],\n    \"teamEvent\": true,\n    \"minSize\": 3,\n    \"maxSize\": 8,\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Why laptop is required?\",\n            \"To code\"\n        ],\n        [\n            \"What are pre-requirements\",\n            \"Have an Hackerrank ID\"\n        ]\n    ],\n    \"category\": [\n        \"Coding\",\n        \"Contest\"\n    ],\n    \"tags\": [\n        \"Prime Event\",\n        \"Special Prizes\"\n    ]\n}"
						}
					]
				},
				{
					"name": "Delete a Particular Event",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "DELETE",
						"header": [
							{
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}"
							]
						},
						"description": "Deleting an event. Only a staff can delete event"
					},
					"response": [
						{
							"name": "Deleting a Event",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/1",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"1"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "Text",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				},
				{
					"name": "Get details for a particular event",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}"
							]
						},
						"description": "Get all details for the event."
					},
					"response": [
						{
							"name": "Get details for a particular event (team event)",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
										"key": "Authorization",
										"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SUQiOiJ0aGlzaWQiLCJzdHVkZW50RW1haWwiOiJyYW1kQGdtYWlsLmNvbSIsImlhdCI6MTU1NDM5NzYyMiwiZXhwIjoxNTU0NDA0ODIyfQ.bfmiEvKyoqP_y0R1yxYHXHWZIduYlyAKRJWHgQt-hM0",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/1",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"1"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"publicId\": \"1\",\n    \"name\": \"Codechef Elektra\",\n    \"eventPicture\":\"some url\",\n    \"eventLogo\":\"some url\",\n    \"description\": \"A 3 hour long competitive coding contest which tests your problem solving and coding skills.\",\n    \"date\": \"2019-09-24\",\n    \"time\": \"09:30\",\n    \"venue\": \"Computer Lab\",\n    \"fees\": 300,\n    \"prize\": [\n        \"First Prize: 2000\",\n        \"Second Prize: 1500\",\n        \"Third Prize: 1000\",\n        \"100 Ladoos to top 15 coders\"\n    ],\n    \"teamEvent\": true,\n    \"teamEventProperties\":{\n    \t\"minSize\": 3,\n    \t\"maxSize\": 8\t\n    },\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Why laptop is required?\",\n            \"To code\"\n        ],\n        [\n            \"What are pre-requirements\",\n            \"Have an Hackerrank ID\"\n        ]\n    ],\n    \"category\": [\n        \"Coding\",\n        \"Contest\"\n    ],\n    \"tags\": [\n        \"Prime Event\",\n        \"Special Prizes\"\n    ]\n}"
						}
					]
				},
				{
					"name": "Edit Event Details",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\": \"Name of the Event\",\n    \"description\": \"Event Description\",\n    \"date\": \"YYYY-MM-DD\",\n    \"time\": \"HH:MM\",\n    \"venue\": \"Event Venue\",\n    \"fees\": \"Participation Fee\",\n    \"prize\": [\"First Prize\", \"Second Prize\", \"Prize for innovation\"],\n    \"teamEvent\": true,\n\t\"teamProperties\":{\n   \t\t\"minSize\": 3,\n    \t\"maxSize\": 8\n\t},\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Question with multiple Answers\",\n            \"Answer1\"\n        ],\n        [\n            \"Put Question 2\",\n            \"Put Answer here\"\n        ]\n    ],\n    \"category\": [\n        \"Defaults to Others\",\n        \"Can be an array of valid categories\"\n    ],\n    \"tags\": [\n        \"Optional\",\n        \"Can be an array of valid tags\"\n    ]\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}"
							]
						},
						"description": "Allow editing of event details. Can edit everything except Id.\n\nIf editing teamEvent field from false to true then must provide maxSize, minSize fields."
					},
					"response": [
						{
							"name": "Update Event Details",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"warning": "This is a duplicate header and will be overridden by the Authorization header generated by Postman.",
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"Elektra 4.0\",\n    \"description\": \"Difficult Questions are waiting for you.\",\n    \"category\": []\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/1",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"1"
									]
								}
							},
							"status": "Accepted",
							"code": 202,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"eventid\": \"1\",\n    \"name\": \"Elektra 4.0\",\n    \"description\": \"Difficult Questions are waiting for you.\",\n    \"date\": \"2019-09-24\",\n    \"time\": \"09:30\",\n    \"venue\": \"Computer Lab\",\n    \"fees\": \"Rs 300\",\n    \"prize\": [\n        \"First Prize: 2000\",\n        \"Second Prize: 1500\",\n        \"Third Prize: 1000\",\n        \"100 Ladoos to top 15 coders\"\n    ],\n    \"teamEvent\": true,\n    \"minSize\": 3,\n    \"maxSize\": 8,\n    \"rules\": [\n        \"Everyone should Participate\",\n        \"Good Work etc etc\"\n    ],\n    \"faq\": [\n        [\n            \"Why laptop is required?\",\n            \"To code\"\n        ],\n        [\n            \"What are pre-requirements\",\n            \"Have an Hackerrank ID\"\n        ]\n    ],\n    \"category\": [\n        \"Others\"\n    ],\n    \"tags\": [\n        \"Prime Event\",\n        \"Special Prizes\"\n    ]\n}"
						}
					]
				},
				{
					"name": "Add/Edit photos for event",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "multipart/form-data",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "picture",
									"type": "file",
									"src": []
								},
								{
									"key": "logo",
									"type": "file",
									"src": []
								}
							]
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/photo",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"photo"
							]
						},
						"description": "Add photos for the event by upload."
					},
					"response": [
						{
							"name": "Add photos for event",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "multipart/form-data",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "picture",
											"type": "file",
											"src": []
										},
										{
											"key": "logo",
											"type": "file",
											"src": []
										}
									]
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/photo",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"photo"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": null,
							"header": null,
							"cookie": [],
							"body": null
						}
					]
				}
			],
			"description": "Event Endpoints. Allow to create new Events, Delete them and update details.",
			"event": [
				{
					"listen": "prerequest",
					"script": {
						"id": "e36221d4-22a4-4275-a2a8-898ebc2dd8b6",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				},
				{
					"listen": "test",
					"script": {
						"id": "2878f61a-91f4-42aa-95b4-5608d56b7831",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				}
			]
		},
		{
			"name": "Event Registration",
			"item": [
				{
					"name": "Get User/Team Registration Details for a Event",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/registrations",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"registrations"
							]
						},
						"description": "Get al registrations for an event"
					},
					"response": [
						{
							"name": "Get Team Registration Details for a Event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/registrations",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"registrations"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": null,
							"cookie": [],
							"body": "{\n    \"eventPublicId\": \"event Id\",\n    \"eventType\": \"team\",\n    \"registrations\": [\n        {\n            \"teamId\": \"abc\",\n            \"status\": \"confirmed\"\n        },\n        {\n            \"teamId\": \"def\",\n            \"status\": \"payment pending\"\n        },\n        {\n            \"teamId\": \"xyz\",\n            \"status\": \"waiting\"\n        }\n    ]\n}"
						},
						{
							"name": "Get User Registration Details for a Event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/registrations",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"registrations"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"eventPublicId\":\"event Id\",\n\t\"eventType\":\"single\",\n\t\"registrations\":[\n\t\t\n\t\t{\n\t\t\t\"registrationId\":\"some id\",\n\t\t\t\"userId\":\"abc\",\n\t\t\t\"status\":\"confirmed\"\n\t\t},\n\t\t{\n\t\t\t\"registrationId\":\"some id\",\n\t\t\t\"userId\":\"def\",\n\t\t\t\"status\":\"payment pending\"\n\t\t},\n\t\t{\n\t\t\t\"registrationId\":\"some id\",\n\t\t\t\"userId\":\"xyz\",\n\t\t\t\"status\":\"waiting\"\n\t\t}\n\t\t\n\t]\n}"
						}
					]
				},
				{
					"name": "Register for an Event",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"teamId\": \"2\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/register/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"register",
								""
							]
						},
						"description": "Register for tem or solo events.\nSend team ID in payload if registerting for team event.\n\nThe team leader must invoke this API"
					},
					"response": [
						{
							"name": "Register for an Event (Successful)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"teamId\": \"2\",\n\t\"action\": \"register\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/register/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"register",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"message\": \"Successfully registered\"\n}"
						},
						{
							"name": "Register for an Event (Already Registered)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"teamId\": \"2\",\n\t\"action\": \"register\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/register/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"register",
										""
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"message\": \"Team already registered for event\",\n\t\"eventId\": \"1\",\n\t\"teamId\": \"2\",\n\t\"status\": \"registered\"\n}"
						}
					]
				},
				{
					"name": "Get registration details",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/registrations/{{registration_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"registrations",
								"{{registration_id}}"
							]
						},
						"description": "Get details of a particular registration"
					},
					"response": [
						{
							"name": "Get registration details",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/registrations/{{registration_id}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"registrations",
										"{{registration_id}}"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": null,
							"cookie": [],
							"body": "{\n    \"registrationId\": \"some id\",\n    \"userId\": \"abc\",\n    \"status\": \"confirmed\"\n}"
						}
					]
				}
			]
		},
		{
			"name": "Teams",
			"item": [
				{
					"name": "Get List of Teams",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{protocol}}://{{hostname}}/teams?limit&page&event&user",
							"protocol": "{{protocol}}",
							"host": [
								"{{hostname}}"
							],
							"path": [
								"teams"
							],
							"query": [
								{
									"key": "limit",
									"value": null,
									"description": "Limit of results returned"
								},
								{
									"key": "page",
									"value": null,
									"description": "Act as an offset for results"
								},
								{
									"key": "event",
									"value": null,
									"description": "Team Id for which team needs to be returned."
								},
								{
									"key": "user",
									"value": null,
									"description": "Reurn teams in which a particular user belongs"
								}
							]
						},
						"description": "Get a List of all the Teams\nCan only be acceses by moderators and superuser\nSupports page view(limit and page)\nCan be Filtered by events, and users\n\nInvitees are the list of pending invitations only.\nMembers are list of team members"
					},
					"response": [
						{
							"name": "Get List of Teams",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{hostname}}/teams?limit=&page=&event=&user",
									"protocol": "{{protocol}}",
									"host": [
										"{{hostname}}"
									],
									"path": [
										"teams"
									],
									"query": [
										{
											"key": "limit",
											"value": "",
											"description": "Limit of results returned"
										},
										{
											"key": "page",
											"value": "",
											"description": "Act as an offset for results"
										},
										{
											"key": "event",
											"value": "",
											"description": "Team Id for which team needs to be returned."
										},
										{
											"key": "user",
											"value": null,
											"description": "Reurn teams in which a particular user belongs"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"pages\": 5,\n\t\"currentpage\": 1,\n\t\"result\": [\n\t\t{\n\t\t\t\"teamid\": \"2\",\n\t\t\t\"leader\": \"user\",\n\t\t\t\"members\": [],\n\t\t\t\"invitees\": [],\n\t\t\t\"events\": [\"1\"]\n\t\t},\n\t\t{\n\t\t\t\"teamid\": \"4\",\n\t\t\t\"leader\": \"user_01\",\n\t\t\t\"members\": [\"23d\", \"user2\", \"user30\"],\n\t\t\t\"invitees\": [],\n\t\t\t\"events\": [\"3\", \"4\"]\n\t\t}\n\t\t]\n}"
						},
						{
							"name": "Get List of Teams by event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams?limit=&page=&event=1&user",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams"
									],
									"query": [
										{
											"key": "limit",
											"value": "",
											"description": "Limit of results returned"
										},
										{
											"key": "page",
											"value": "",
											"description": "Act as an offset for results"
										},
										{
											"key": "event",
											"value": "1",
											"description": "Team Id for which team needs to be returned."
										},
										{
											"key": "user",
											"value": null,
											"description": "Reurn teams in which a particular user belongs"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"pages\": 2,\n\t\"currentpage\": 1,\n\t\"result\": [\n\t\t{\n\t\t\t\"teamid\": \"2\",\n\t\t\t\"leader\": \"user\",\n\t\t\t\"members\": [],\n\t\t\t\"invitees\": [],\n\t\t\t\"events\": [\"1\"]\n\t\t},\n\t\t{\n\t\t\t\"teamid\": \"4\",\n\t\t\t\"leader\": \"user_01\",\n\t\t\t\"members\": [\"23d\", \"user2\", \"user30\"],\n\t\t\t\"invitees\": [],\n\t\t\t\"events\": [\"1\"]\n\t\t}\n\t\t]\n}"
						}
					]
				},
				{
					"name": "Create a new Team",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"name\":\"The Gingers\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								""
							]
						},
						"description": "Create a Team.\nThe person to create team automatically becomes the new team leader."
					},
					"response": [
						{
							"name": "Create a Team",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"name\": \"The Gingers\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"teamid\": \"1\",\n\t\"name\": \"The Gingers\",\n    \"leader\": \"test_user_001\",\n    \"members\": [],\n    \"events\": [],\n    \"invitees\": []\n}"
						}
					]
				},
				{
					"name": "Delete a Team",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								"{{team_id}}"
							]
						},
						"description": "Deleting a Team\nWill also unregister it from the participated events."
					},
					"response": [
						{
							"name": "Delete a Team",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				},
				{
					"name": "Edit Team Details",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\": \"The Flockers\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								"{{team_id}}"
							]
						},
						"description": "Editing Team Details\nCan Change Team Leader"
					},
					"response": [
						{
							"name": "Edit Team Details",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"The Flockers\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}?",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}"
									],
									"query": [
										{
											"key": "",
											"value": "",
											"disabled": true
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"teamid\": \"1\",\n    \"name\": \"The Flockers\",\n    \"leader\": \"test_user_002\",\n    \"members\": [\"username_01\", \"username_02\"],\n    \"event\": [\"1\", \"3\"],\n    \"invitees\": []\n}"
						}
					]
				},
				{
					"name": "Get Details of a Particular Team",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								"{{team_id}}"
							]
						},
						"description": "Get Details of a Single Team"
					},
					"response": [
						{
							"name": "Get Details of a Particular Team",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\t\t\"teamid\": \"4\",\n\t\t\t\"leader\": \"user_01\",\n\t\t\t\"members\": [\"23d\", \"user2\", \"user30\"],\n\t\t\t\"invitees\": [],\n\t\t\t\"events\": [\"1\"]\n}"
						}
					]
				},
				{
					"name": "View Team Invitations",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"invitation"
							]
						},
						"description": "View Invitations recieved by a particular user. Includes accepted and rejected invitations."
					},
					"response": [
						{
							"name": "View Team Invitations",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": ""
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"teamid\": \"1\",\n\t\t\"name\": \"The Rookies\",\n\t\t\"leader\": \"1\",\n\t\t\"status\": \"accepted\"\n\t},\n\t{\n\t\t\"teamid\": \"2\",\n\t\t\"name\": \"The Sweet\",\n\t\t\"leader\": \"2\",\n\t\t\"status\": \"rejected\"\n\t},\n\t{\n\t\t\"teamid\": \"4\",\n\t\t\"name\": \"The Three Musketeers\",\n\t\t\"leader\": \"2\",\n\t\t\"status\": \"pending\"\n\t}\n]"
						}
					]
				},
				{
					"name": "Accept Team Invitation",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation/{{team_id}}/accept/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"invitation",
								"{{team_id}}",
								"accept",
								""
							]
						},
						"description": "Accept Invitation and join team. If already joined then responds with error."
					},
					"response": [
						{
							"name": "Accept Team Invitation (Error)",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation/{{team_id}}/accept/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"invitation",
										"{{team_id}}",
										"accept",
										""
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"error\": \"Already Accepted\"\n}"
						},
						{
							"name": "Accept Team Invitation",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation/{{team_id}}/accept/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"invitation",
										"{{team_id}}",
										"accept",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"status\": \"invitation accepted\",\n\t\"teamid\": \"1\",\n\t\"name\": \"The Rookies\"\n}"
						}
					]
				},
				{
					"name": "Reject Team Invitation",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation/{{team_id}}/reject/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"users",
								"{{username}}",
								"invitation",
								"{{team_id}}",
								"reject",
								""
							]
						},
						"description": "Reject Invitation and join team. If already rejected then responds with error."
					},
					"response": [
						{
							"name": "Reject Team Invitation",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/users/{{username}}/invitation/{{team_id}}/reject/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"users",
										"{{username}}",
										"invitation",
										"{{team_id}}",
										"reject",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"status\": \"invitation rejectedd\",\n\t\"teamid\": \"1\",\n\t\"name\": \"The Rookies\"\n}"
						}
					]
				},
				{
					"name": "New Team Invitation",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\": \"test_user_001\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{hostname}}/teams/{{team_id}}/invitations",
							"protocol": "{{protocol}}",
							"host": [
								"{{hostname}}"
							],
							"path": [
								"teams",
								"{{team_id}}",
								"invitations"
							]
						},
						"description": "Create a new invitation. Can only invite a member from same college. Also gives error if person is already invited."
					},
					"response": [
						{
							"name": "New Team Invitation (Error)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\": \"WrongId\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{hostname}}/teams/{{team_id}}/invitations",
									"protocol": "{{protocol}}",
									"host": [
										"{{hostname}}"
									],
									"path": [
										"teams",
										"{{team_id}}",
										"invitations"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"error\": \"Not from same college/Already invited/Already a member/Wrong Username\"\n}"
						},
						{
							"name": "New Team Invitation (Success)",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"username\": \"test_user_001\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{hostname}}/teams/{{team_id}}/invitations",
									"protocol": "{{protocol}}",
									"host": [
										"{{hostname}}"
									],
									"path": [
										"teams",
										"{{team_id}}",
										"invitations"
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"teamid\": \"1\",\n\t\"name\": \"The Gingers\",\n\t\"leader\": \"User\",\n\t\"members\": [\"user_001\", \"user_002\"],\n\t\"invitees\": [\"test_user_001\", \"test_user_003\"],\n\t\"events\": []\n}"
						}
					]
				},
				{
					"name": "Delete Member",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								"{{team_id}}",
								"{{username}}"
							]
						},
						"description": "Delete a member from team."
					},
					"response": [
						{
							"name": "Delete Member",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}",
										"{{username}}"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				},
				{
					"name": "Delete Invitation",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}/invitations/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"teams",
								"{{team_id}}",
								"invitations",
								"{{username}}"
							]
						},
						"description": "Delete a unaccepted invitation. If invitation does not exist or its already accepted/rejected then gives error."
					},
					"response": [
						{
							"name": "Delete Invitation (Error)",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}/invitations/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}",
										"invitations",
										"{{username}}"
									]
								}
							},
							"status": "Unprocessable Entity (WebDAV) (RFC 4918)",
							"code": 422,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"error\": \"Does not exist/ Already Accepted\"\n}"
						},
						{
							"name": "Delete Member",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"type": "text",
										"value": "application/json"
									},
									{
										"key": "Authorization",
										"type": "text",
										"value": "Bearer {{access_token}}"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/teams/{{team_id}}/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"teams",
										"{{team_id}}",
										"{{username}}"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				}
			]
		},
		{
			"name": "Tickets",
			"item": [
				{
					"name": "View all Tickets",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/ticket?limit&page&user&topic&status",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"ticket"
							],
							"query": [
								{
									"key": "limit",
									"value": null
								},
								{
									"key": "page",
									"value": null
								},
								{
									"key": "user",
									"value": null,
									"description": "Username who raised the ticket."
								},
								{
									"key": "topic",
									"value": null,
									"description": "Keyword in tickets title."
								},
								{
									"key": "status",
									"value": null,
									"description": "solved or unsolved"
								}
							]
						},
						"description": "All the tickets. Only for staff users."
					},
					"response": [
						{
							"name": "View all Tickets",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/ticket?limit=2&page=1",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"ticket"
									],
									"query": [
										{
											"key": "limit",
											"value": "2"
										},
										{
											"key": "page",
											"value": "1"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"pages\": 2,\n    \"currentpage\": 1,\n    \"result\": [\n        {\n            \"ticketid\": \"23\",\n            \"title\": \"New Issue\",\n            \"description\": \"Fix it Fast\",\n            \"openedBy\": \"sample_user_id\",\n            \"openingdate\": \"2019-12-1\",\n            \"solution\": {\n                \"status\": \"solved\",\n                \"solvedBy\": \"user_233\",\n                \"solvingDate\": \"2019-12-30\",\n                \"content\": \"This is a simple issue. It is solved.\"\n            }\n        },\n        {\n            \"ticketid\": \"34\",\n            \"title\": \"Another Issue\",\n            \"description\": \"Fix it Faster\",\n            \"openedBy\": \"sample_user_id\",\n            \"openingDate\": \"2019-11-29\",\n            \"solution\": {\n                \"status\": \"unsolved\"\n            }\n        }\n    ]\n}"
						}
					]
				},
				{
					"name": "View Public Tickets",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/ticket/public?limit&page&status=&topic",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"ticket",
								"public"
							],
							"query": [
								{
									"key": "limit",
									"value": null
								},
								{
									"key": "page",
									"value": null
								},
								{
									"key": "status",
									"value": "",
									"description": "solved or unsolved"
								},
								{
									"key": "topic",
									"value": null,
									"description": "keyword in the title"
								}
							]
						},
						"description": "All Public Tickets view. Open for all."
					},
					"response": [
						{
							"name": "View Public Tickets",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/ticket/public?limit&page&status=solved",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"ticket",
										"public"
									],
									"query": [
										{
											"key": "limit",
											"value": null
										},
										{
											"key": "page",
											"value": null
										},
										{
											"key": "status",
											"value": "solved"
										}
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Accept",
									"value": "application/json",
									"description": "",
									"type": "text"
								}
							],
							"cookie": [],
							"body": "{\n    \"pages\": 2,\n    \"currentpage\": 1,\n    \"result\": [\n        {\n            \"ticketid\": \"23\",\n            \"title\": \"New Issue\",\n            \"description\": \"Fix it Fast\",\n            \"openedBy\": \"sample_user_id\",\n            \"openingdate\": \"2019-12-1\",\n            \"solution\": {\n                \"status\": \"solved\",\n                \"solvedBy\": \"user_233\",\n                \"solvingDate\": \"2019-12-30\"\n                \"content\": \"Solved Issue\",\n            }\n        }\n    ]\n}"
						}
					]
				},
				{
					"name": "View User Ticket",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/ticket/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"ticket",
								"{{username}}"
							]
						},
						"description": "Tickets raised by a particular user. Public/Private both."
					},
					"response": [
						{
							"name": "View User Ticket",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/ticket/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"ticket",
										"{{username}}"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n    \"pages\": 2,\n    \"currentpage\": 1,\n    \"result\": [\n        {\n            \"ticketid\": \"23\",\n            \"title\": \"New Issue\",\n            \"description\": \"Fix it Fast\",\n            \"openedBy\": \"sample_user_id\",\n            \"openingdate\": \"2019-12-1\",\n            \"solution\": {\n                \"status\": \"solved\",\n                \"solvedBy\": \"user_233\",\n                \"solvingDate\": \"2019-12-30\",\n                \"content\": \"Solution\"\n           \n            }\n        }\n    ]\n}"
						}
					]
				},
				{
					"name": "Open a Tiicket",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"title\": \"Another Issue\",\n    \"description\": \"Fix it Faster\",\n    \"view\": \"public or private\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/ticket/",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"ticket",
								""
							]
						},
						"description": "Open a new ticket by user."
					},
					"response": [
						{
							"name": "Open a Tiicket",
							"originalRequest": {
								"method": "POST",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"title\": \"New Issue\",\n\t\"description\": \"Fix it Fast\",\n\t\"view\": \"public\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/ticket/",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"ticket",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"ticketid\": \"34\",\n    \"title\": \"New Issue\",\n    \"description\": \"Fix it Fast\",\n    \"openedBy\": \"sample_user_id\",\n    \"openingDate\": \"2019-11-29\",\n    \"solution\": {\n    \t\"status\": \"unsolved\"\n    }\n}"
						}
					]
				},
				{
					"name": "Close a Ticket",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							},
							{
								"key": "Content-Type",
								"name": "Content-Type",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"content\": \"This is my solution\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/ticket/{{ticket_id}}/close",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"ticket",
								"{{ticket_id}}",
								"close"
							]
						},
						"description": "Close a ticket (Solve a issue). Only for staff users."
					},
					"response": [
						{
							"name": "Close a Ticket",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									},
									{
										"key": "Content-Type",
										"name": "Content-Type",
										"value": "application/json",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"content\": \"This is my solution\"\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/ticket/{{ticket_id}}/close",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"ticket",
										"{{ticket_id}}",
										"close"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"ticketid\": \"23\",\n    \"title\": \"New Issue\",\n    \"description\": \"Fix it Fast\",\n    \"openedBy\": \"sample_user_id\",\n    \"openingdate\": \"2019-12-1\",\n    \"solution\": {\n    \t\"status\": \"solved\",\n    \t\"solvedBy\": \"user_233\",\n    \t\"solvingDate\": \"2019-12-30\",\n    \t\"content\": \"This is my solution\"\n    }\n}"
						}
					]
				}
			]
		},
		{
			"name": "Organisers",
			"item": [
				{
					"name": "Get organisers for a event",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"organisers"
							]
						},
						"description": "Returns list of all organisers for the event."
					},
					"response": [
						{
							"name": "Get organisers for a event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"organisers"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"username\": \"test_user_001\",\n\t\t\"role\": \"Lead Member\"\n\t},\n\t{\n\t\t\"username\": \"test_user_003\",\n\t\t\"role\": \"Member\"\n\t},\n\t{\n\t\t\"username\": \"test_user_002\",\n\t\t\"role\": \"Head\"\n\t}\n]"
						}
					]
				},
				{
					"name": "Add a new organiser",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\": \"user_001\",\n\t\"role\": \"role\"\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"organisers"
							]
						}
					},
					"response": [
						{
							"name": "Add a new organiser",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"organisers"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n    {\n        \"username\": \"user\",\n        \"role\": \"Member\"\n    },\n    {\n        \"username\": \"user_001\",\n        \"role\": \"Leader\"\n    },\n    {\n        \"username\": \"user_002\",\n        \"role\": \"Head of Comittee\"\n    },\n    {\n        \"username\": \"user_004\",\n        \"role\": \"Member\"\n    }\n]"
						}
					]
				},
				{
					"name": "Delete a Organiser",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"organisers",
								"{{username}}"
							]
						}
					},
					"response": [
						{
							"name": "Delete a Organiser",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/organisers/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"organisers",
										"{{username}}"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "Text",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				}
			]
		},
		{
			"name": "Volunteers",
			"item": [
				{
					"name": "Get Volunteers for a event",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{access_token}}"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"volunteers"
							]
						},
						"description": "Returns list of all volunteers for the event."
					},
					"response": [
						{
							"name": "Get volunteers for a event",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"volunteers"
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"username\": \"test_user_001\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t},\n\t{\n\t\t\"username\": \"test_user_003\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t},\n\t{\n\t\t\"username\": \"test_user_002\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t}\n]"
						}
					]
				},
				{
					"name": "Add a new volunteers",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Accept",
								"type": "text",
								"value": "application/json"
							},
							{
								"key": "Authorization",
								"type": "text",
								"value": "Bearer {{staff_access_token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"username\": \"user_5\",\n\t\"task\": [\"Arrange Rooms\", \"Take Attendence\"]\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"volunteers"
							]
						}
					},
					"response": [
						{
							"name": "Add a new volunteer",
							"originalRequest": {
								"method": "GET",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"volunteers"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "[\n\t{\n\t\t\"username\": \"test_user_001\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t},\n\t{\n\t\t\"username\": \"test_user_003\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t},\n\t{\n\t\t\"username\": \"test_user_002\",\n\t\t\"task\": [\"Do this\", \"Do that\"]\n\t},\n\t{\n\t\"username\": \"user_5\",\n\t\"task\": [\"Arrange Rooms\", \"Take Attendence\"]\n\t}\n]"
						}
					]
				},
				{
					"name": "Delete a Volunteer",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"volunteers",
								"{{username}}"
							]
						}
					},
					"response": [
						{
							"name": "Delete a Organiser",
							"originalRequest": {
								"method": "DELETE",
								"header": [
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"volunteers",
										"{{username}}"
									]
								}
							},
							"status": "No Content",
							"code": 204,
							"_postman_previewlanguage": "Text",
							"header": [],
							"cookie": [],
							"body": ""
						}
					]
				},
				{
					"name": "Change Tasks for Volunteer",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{staff_access_token}}",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n\t\"task\": [\"Task1\", \"Task2\"]\n}"
						},
						"url": {
							"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers/{{username}}",
							"protocol": "{{protocol}}",
							"host": [
								"{{host_name}}"
							],
							"path": [
								"events",
								"{{event_id}}",
								"volunteers",
								"{{username}}"
							]
						}
					},
					"response": [
						{
							"name": "Change Tasks for Volunteer",
							"originalRequest": {
								"method": "PUT",
								"header": [
									{
										"key": "Content-Type",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Accept",
										"value": "application/json",
										"type": "text"
									},
									{
										"key": "Authorization",
										"value": "Bearer {{staff_access_token}}",
										"type": "text"
									}
								],
								"body": {
									"mode": "raw",
									"raw": "{\n\t\"task\": [\"task1\", \"task2\"]\n}"
								},
								"url": {
									"raw": "{{protocol}}://{{host_name}}/events/{{event_id}}/volunteers/{{username}}",
									"protocol": "{{protocol}}",
									"host": [
										"{{host_name}}"
									],
									"path": [
										"events",
										"{{event_id}}",
										"volunteers",
										"{{username}}"
									]
								}
							},
							"_postman_previewlanguage": "json",
							"header": [],
							"cookie": [],
							"body": "{\n\t\"eventid\": \"2\",\n\t\"volunteer\": \"user_01\",\n\t\"task\": [\"task1\", \"task2\"]\n}"
						}
					]
				}
			],
			"event": [
				{
					"listen": "prerequest",
					"script": {
						"id": "ca75cef1-89aa-4254-b12f-1c6bf17a3b44",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				},
				{
					"listen": "test",
					"script": {
						"id": "0d9e14da-4a99-4afb-ada7-383990f0987f",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				}
			]
		}
	],
	"event": [
		{
			"listen": "prerequest",
			"script": {
				"id": "e8a006b1-ae04-485c-984b-b1039b2706e7",
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"id": "6fb5002c-c660-4c76-881e-1f29480bd8fa",
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		}
	]
}