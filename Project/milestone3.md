<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Koushik Chandrasekaran (kc664)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 2:20:18 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/kc664" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236394134-c0129c74-25ff-497d-bb93-50fc23a1b08b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Orders Table from DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236394268-4161060d-e8c1-4710-b42d-b4199241facb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of OrderItems Table from DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236395105-3cc94501-b7df-4886-a88d-01a4273f6294.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase form UI from Heroku with valid data filled in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236395427-295105d6-b389-4de4-a36d-29adb490b9a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pending Purchase form with valid data filled in. Here, the user cannot edit<br>quantity of items. The form also has a link to go back to<br>cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236396689-f7585ad6-ae0c-4084-b625-3789574a7450.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation to check if address and payment details are filled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236396889-243b7e9f-9e1d-4f62-99a0-419ac09c6594.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation to check if the amount paid matches total cart amount. We also<br>check if stock, and price of items are correct.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236397560-d1a62bac-7f68-4311-9b45-5f436eb1d2e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample payment (order process) done with wrong amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236397781-9f8a43c5-cf0c-44c5-ab46-d53685d3b657.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message shown when amount paid doesn&#39;t match cart&#39;s total amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236398598-9db295f3-1777-4b4f-bcb1-71958875541b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Trying to update quantity of &quot;Lamzu Atlantis Mini (White)&quot; from 1 to 15<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236398969-49054400-fb5e-4902-8acb-f67adfd53df4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error thrown while updating quantity since the number exceeds the stock <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236399346-39e9e9e6-16fa-4643-9e82-32dcede9273e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin updates price of &quot;Gigabyte GeForce RTX 4090&quot; from 1700 to 1799<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236399561-91a2697c-cb99-4675-bad6-afa99f97aa5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message shown to the user when they try to place an order<br>and the item&#39;s price has changed from previous value. The cart is refreshed<br>and the amount is updated for the user.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>The user first selects items from the shop along with the quantities.<br>The items are then listed along with their quantities and costs (subtotals) in<br>the cart page.&nbsp;<div>2) The user will be directed to confirm order page when<br>the place order button is clicked on cart page.</div><div>3) In the confirm order<br>page, users can verify the details of their cart. If the details are<br>correct and the items are in stock, the user can enter their shipping<br>address and payment details to make the payment. Else, the user is redirected<br>to cart page to refresh their cart.</div><div>4) If all the details are correct,<br>and the payment is successful, the order will be confirmed.&nbsp;</div><div>5) The backend again<br>verifies the stock and price. If the validation succeeds, entries are made into<br>the Orders for each order by a user, and OrderItems table for each<br>item purchased.</div><div>6) If there are no issues from above, the items are removed<br>from the cart table, and the stock of those items is updated in<br>the backend.</div><div>7) The user is presented with a summary of their order details<br>along with the Order ID.</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/65">https://github.com/CK-ghub/IS601-004/pull/65</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/confirm_order">https://is601-kc664-project-prod.herokuapp.com/confirm_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236462242-03b6374c-1ab9-4d22-90b1-6af4a65fef61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order confirmation page with all the requirements satisfied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>Once the user clicks on the place order button on cart page, the<br>user is directed to a confirmation page where address and payment information is<br>required. Once these details are filled by the user, they are added to<br>the orders table in the backend when the order goes through successfully. When<br>the order is confirmed, these details are fetched and rendered as a table<br>in the frontend.&nbsp;<div>The same is done for OrderItems table where each purchased item<br>along with the quantities are added to and retrieved from the table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/66">https://github.com/CK-ghub/IS601-004/pull/66</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/place_order">https://is601-kc664-project-prod.herokuapp.com/place_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236521994-8a8aa0fb-facf-4793-97e6-ae8bb31e6070.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of order listings page for a user showing their purchase history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236522270-942fef0f-79c5-4b4a-ad30-6f740c8272dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of order details page showing full details of a purchaseF<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>A user can view their purchase history by clicking on Orders in navigation<br>bar. When an user tries to view their orders, all the details are<br>fetched from the orders table with an user id filter. Each item in<br>this list has a View button. When this button is clicked, data is<br>fetched from both orders table and orderitems table by a join operation on<br>order id and user id. This is done to ensure that a user<br>cannot see other user&#39;s purchase history. After joining them, the items ordered in<br>a particular order along with the shipping address and billing information is displayed<br>in tables.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/67">https://github.com/CK-ghub/IS601-004/pull/67</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/orders">https://is601-kc664-project-prod.herokuapp.com/orders</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/order?id=83">https://is601-kc664-project-prod.herokuapp.com/order?id=83</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236533714-f0434a4a-a106-4d0c-a30c-7ae08126000e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of purchase history from multiple users. A view button is also included<br>to view that particular order in detail. In addition, the username of a<br>person is also shown for each order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236534600-4f671d4a-cf9c-444f-90e4-2696d9656eec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order details of a user that is not admin/store owner<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>A user&#39;s purchase history is unique to that user while the admin/store owner&#39;s<br>orders history shows all the orders that are placed by multiple users and<br>each order shows the username of the person that placed the order. Logically,<br>both are similar, but the main change here is the initial SQL query<br>for fetching the order details. The orders table is joined with the users<br>table in order to fetch the username. When the view button is clicked,<br>data is fetched from both orders table and orderitems table by a join<br>operation on item id. Here user id is not used since this access<br>is done by an admin/store owners only.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/68">https://github.com/CK-ghub/IS601-004/pull/68</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/admin/order?id=8">https://is601-kc664-project-prod.herokuapp.com/admin/order?id=8</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/236526064-d9f64a51-e377-4df4-9f85-2f5da2252a65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart page having a button to place an order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I faced a major issue when a user tried to place an order<br>from the cart but the price had been changed by the admin. I<br>solved this by using simple IF constructs to compare the cart price and<br>the unit price from the items table, and if were not equal, I<br>redirected to the cart page and refreshed the cart with the updated amount.<br>I also faced another issue while trying to send the data from pending<br>purchase page to confirmation page. Initially, I tried to fix this by sending<br>form elements from one page to another, and this didn&#39;t work since one<br>of the pages worked on GET method. Finally, I fixed this problem by<br>using multiple redirects since the form data is not cleared when the request<br>is redirected. Frontend work was again quite tedious since I had to cleanup<br>everything after Milestone2. Apart from that, I also learned to create different user<br>roles and change page views and functionalities based on their roles accordingly.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/kc664" target="_blank">Grading</a></td></tr></table>