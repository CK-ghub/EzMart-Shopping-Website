<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Koushik Chandrasekaran (kc664)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 11:52:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/kc664" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664120-0a2d0def-d860-4fca-b470-13ebd19c691b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Email Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664215-fce03fa4-3dcd-45f4-9ab4-4cd51eb7dcef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664353-72d1da80-2cfb-4185-966d-15718abed202.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords must match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664505-255983bd-8b2e-4fd8-8565-008a1a244a42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664685-a8fb29e4-415e-4577-9dd0-396694c3dec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232664833-b176dc34-b5ed-41c2-b80b-23998e0a6c08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232665015-6c42b484-526e-4b77-8934-4b6f3446ab2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232665116-1bbd4c5c-c97b-4b12-b300-8506b6cebba3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of users table after inserting user &quot;demo1&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/39">https://github.com/CK-ghub/IS601-004/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We use WTForms, a Python library,&nbsp; to create and validate HTML forms. It<br>comes with in-built validators that can show error messages on the frontend to<br>prevent unwanted requests to the backend.&nbsp;The unique username, email validations are done in<br>the backend by processing the error message from the database. The database has<br>constraints on the username and email. Constraints are also applied to the database<br>to ensure data integrity. Passwords are encrypted using bcrypt before being stored in<br>the database, with a salt value. The hash of salt+password is stored in<br>the database. Finally, database queries are made using a helper function and the<br>results are served on the frontend.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232669040-a73ee0b1-723a-498c-b130-2518afce1080.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232669255-c9d08a54-8ff1-4920-842a-c09833b91050.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid user valdiation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232669461-e4fa53a8-81a0-4cf3-a8b1-d670611b7f5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/41">https://github.com/CK-ghub/IS601-004/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We use WTForms, a Python library,&nbsp; to create and validate HTML forms. It<br>comes with in-built validators that can show error messages on the frontend to<br>prevent unwanted requests to the backend.&nbsp;The unique username, email validations are done in<br>the backend by processing the error message from the database. The database has<br>constraints on the username and email. Constraints are also applied to the database<br>to ensure data integrity. Passwords are encrypted using bcrypt before being stored in<br>the database, with a salt value. The hash of salt+password is stored in<br>the database. Finally, database queries are made using a helper function and the<br>results are served on the frontend.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232670634-4f1d433f-ca56-4857-9b1f-01e2786528a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful logout<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232670783-c900bd85-28f3-49af-9264-e0dd54c429dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out user is not able to access login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/42">https://github.com/CK-ghub/IS601-004/pull/42</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In Flask, sessions can be maintained using built-in methods. Flask uses &quot;flask_login&quot; to<br>maintain the current session and the &quot;current_user&quot; function to keep track of the<br>currently logged-in user&#39;s information. This information is used across web pages to ensure<br>that the user remains logged in. The &quot;current_user&quot; function retrieves the user ID<br>and roles, which are then maintained across pages.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232671711-1cfd14af-516c-4cce-b10b-9e787394a384.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out user is not able to access login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232671896-f4be2de8-99e8-4854-9b9e-d139b4aa5e3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User without proper role is not able to access role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232672225-5bea8cb7-0a04-44a4-868c-8a62343445f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with admin and cookies (example) role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232672532-44300918-8adc-4b9c-aa9a-6395db2a176b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> UserRoles table with assignments (first is admin)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/43">https://github.com/CK-ghub/IS601-004/pull/43</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/44">https://github.com/CK-ghub/IS601-004/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For login-protected pages we use the inbuilt decorator called login_required. This checks if<br>a user is authenticated or not.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>For role-protected pages we fetch the roles attached to the session of the<br>user and see if it matches the desired roles. We use flask's inbuilt<br>permission requirement decorator to check the same.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232674230-12cf09fe-a8ab-4dd9-9a1b-2aa51d6a915d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation bar styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232674891-e93dfc49-faa1-4ff6-805a-e4ab6ad9cfed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed form and table style<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/43">https://github.com/CK-ghub/IS601-004/pull/43</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Changed the background color of navbar and form by using hex codes or<br>named colors in the CSS properties. These rules can be added to the<br>web page&#39;s CSS file or style block.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232682007-ea843be8-f9cc-42da-9274-c0c35d9fd0f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized user accessing a protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232682560-73d5e45f-4308-498c-9580-b634b5e31627.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied for the user to access a role-based page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232682671-37f5259b-4825-4c93-8aec-08103c686ee5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page not found error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232683364-e241b276-443b-4ec5-981f-d0617e5633b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password must match validation <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/44">https://github.com/CK-ghub/IS601-004/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>Using templates we implement status codes 401, 404, 403 and override the default<br>page for status codes. For exceptions, we use regex to see if the<br>message matches the desired format.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232686017-0314943d-1e03-47e0-8e0a-cb636e0ad4fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username and email prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/45">https://github.com/CK-ghub/IS601-004/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span lang="EN-IN">A request is sent to an endpoint with form<br>data. When the<br>endpoint receives the request, it checks whether any data is<br>present in the form.<br>If data is available, it retrieves and displays the data.<br>However, if no data<br>is available, the endpoint displays empty values.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232691439-a85420de-f325-4973-991f-420e6eecba32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232693033-e1293422-b6f2-4b2c-a6bf-760affa13ac5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232693454-44d695db-e10e-4c44-a43e-18ccc41232a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232693995-7ba67ab5-67c6-441c-9226-cea91c855c3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords must match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232694438-d9932866-f1bc-4921-b437-dd5d34405b84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email already chosen validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232695362-d4df30c0-4318-4afa-9277-fa84c612b9ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User table before updating profile data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/232695660-f869b5f3-789c-4ad5-b61a-7f6971fcc162.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User table after updating profile data (email and password)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/46">https://github.com/CK-ghub/IS601-004/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span lang="EN-IN">For email and username, update calls are<br>made to the table by<br>using&nbsp;</span>the user_id as the key. If the username or<br>email already exists in the<br>table, the update query will fail<br>because of the table constraints. In addition, I<br>learned to add desired frontend styling using CSS for forms. In addition faced<br>an issue while trying to incorporate login method. It was throwing an error<br>that current_user is unavailable. Later, I discovered that login manager was not initialized<br>in main.py</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;I learned to use WTForms that have in-built validators to show error messages<br>on the frontend and prevent unwanted requests to the backend.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/login">https://is601-kc664-project-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/kc664" target="_blank">Grading</a></td></tr></table>