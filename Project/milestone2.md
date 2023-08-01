<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Koushik Chandrasekaran (kc664)</td></tr>
<tr><td> <em>Generated: </em> 4/25/2023 9:14:59 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/kc664" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234112798-1c57e56c-401c-4876-b100-5734973acc83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data filled in admin create item page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234113590-a6bd00f1-c2f3-4822-90e7-8e65873c8e08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of added/created products in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>Using HTML forms, we receive the input as form data. The data is<br>verified and validated using WTForms, and then inserted in the DB in the<br>backend using a insert SQL statement. In addition, visibility is set as 1<br>if stock(item)&gt;0, else set as 0.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/49">https://github.com/CK-ghub/IS601-004/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/admin/additem">https://is601-kc664-project-prod.herokuapp.com/admin/additem</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234162481-be1bfb30-179e-4540-b077-3026356191c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of shop page without filters/sorting applied (description of products is reduced to<br>200 characters)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234162790-a7cd8124-14d3-4266-96ea-570e26b31367.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of shop page filtered by &quot;men&quot; with costs in descending order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234163361-04d2bf2c-6e72-4388-84f3-e07135f098c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of filter/sort logic from code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>In the shop page, all products with visibility 1 are fetched, and in<br>addition, filters and order by is applied. For name and description, like filters<br>are used. For sorting, order by SQL command is used where the user<br>can specify if the items are to be displayed in ascending or descending<br>order based on the filter attribute.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/50">https://github.com/CK-ghub/IS601-004/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/shop">https://is601-kc664-project-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234164495-e95f8dad-0398-4310-aa45-75713008167f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin&#39;s view of list of products showing both visible and non visible products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>In this page, we get the admin&#39;s view of the list of products<br>regardless of their visibility. The results are retrieved using a SELECT SQL command<br>with all the columns included with a limit value of 100 and no<br>other filters.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/51">https://github.com/CK-ghub/IS601-004/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/admin/viewitems">https://is601-kc664-project-prod.herokuapp.com/admin/viewitems</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234225945-f44bced6-c81e-4c48-be81-7d5b076cba82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Public shop page showing edit buttons visible only to the admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234226344-df26a8b5-2a1a-4793-a62e-fde0d2ba8fb3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit button visible on product&#39;s view page only for admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234229878-b539df6c-394e-4eb1-8bef-5e87c399f26e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit button visible only to the admin on the Admin Product List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234230516-02f12b78-0ed7-48aa-b647-7162425583e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing product &quot;Gigabyte GeForce RTX 4090&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234230941-62554255-2223-4130-9f99-d22c16d88d5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing product &quot;Gigabyte GeForce RTX 4090&quot; - changed stock from 0 to<br>5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234232098-8fe0f53a-1902-49c1-9176-86fa665ff870.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product &quot;Gigabyte GeForce RTX 4090&quot; is now visible in the shop page (since<br>visibility is now 1)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>All edit buttons have been defined using the &lt;a&gt; tag and the default<br>hyperlink that takes product id in the url.<div>The forms are prefilled by querying<br>the DB. If any field is changed, an update call is made in<br>the backend and additionally, for each edit call, we check if the stock<br>is 0, if yes, we set visibility to 0, else set as 1.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/55">https://github.com/CK-ghub/IS601-004/pull/55</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/admin/viewitems">https://is601-kc664-project-prod.herokuapp.com/admin/viewitems</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234235381-f5dc15e6-a90b-448e-b6e8-bdc23e370a66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page with clickable view buttons<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234235706-86c95eb5-73c7-4dbe-a991-1cf436f8c0e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product details page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>When a user clicks on the view button, a call is made to<br>the view_item endpoint in the shop blueprint along with the product id. In<br>the backend, relevant data is fetched from DB and displayed in the frontend<br>using the product id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/56">https://github.com/CK-ghub/IS601-004/pull/56</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/shop/item?id=7">https://is601-kc664-project-prod.herokuapp.com/shop/item?id=7</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234269772-7a23dd6a-63e8-4ed1-b780-247dc0324e6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message shows item has been added to cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234269997-7b5ded90-9534-4fe4-b4f6-47ab42fc4a8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added item in cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234272169-4a5bf87a-f960-4cdd-9bf5-bf10cfbd61e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message when user tries to access cart without logging in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234272759-bfa5db23-c44a-4300-9511-ba3c360b76bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart table with some data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>Each user can have only one cart at a time. Once the order<br>is placed, the cart is cleared. The quantity is chosen from the shop<br>page by users when adding an item to cart (by default 1). Users<br>can also edit the quantity of the items in their cart at any<br>time.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>When an user clicks on add to cart button, that particular item is<br>added to their cart.</div><div><br></div><div>In the backend, cart table has an item inserted for<br>that particular item. One user will have multiple entries in the cart table.<br>Each row in the table is associated to each item in their cart.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/57">https://github.com/CK-ghub/IS601-004/pull/57</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234281419-44a20a8d-fe8c-4cae-acc6-8c08a6a345c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart page with all the above requirements satisfied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>After the cart items are fetched from the db, the subtotal is calculated<br>in the frontend by multiplying the unit price with the quantity. This is<br>shown as subtotal. In the frontend, all the subtotal values are added and<br>displayed in the end as total. Namespaces are used in the frontend to<br>ensure that the scope of the total object is available till the end.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/59">https://github.com/CK-ghub/IS601-004/pull/59</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/cart">https://is601-kc664-project-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234283103-9a2c64a9-20f5-44a0-841b-e939a3603cc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart before updating quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234283452-fd6b9acb-e23c-4c36-9b16-7ec74b6f49e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Quantity of &quot;Apple AirPods Pro (2nd Gen)&quot; updated from 1 to 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234284013-65714ebd-20a4-46ee-b784-38e9a5d53a90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before setting cart quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234284386-1ef21d23-6d8b-44ca-8f6a-ef3e6f8b1b6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Quantity of &quot;Apple AirPods Pro (2nd Gen)&quot; updated from 2 to 0 -<br>item deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234285110-30472887-e112-47b6-afd2-b55fc4725cd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart before updating quantity to negative<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234285306-567fe6bc-e908-45da-9f3c-48a8c9b7478c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart after setting quantity of &quot;Greenlights Hardcover&quot; to -1 (item gets deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>When an user sets the quantity as 0 or a negative values, it<br>is considered as item deletion in the backend. i.e that particular item is<br>deleted from the cart of that particular user.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/60">https://github.com/CK-ghub/IS601-004/pull/60</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234286533-76787c2d-2c0f-4593-9238-59ba0cff8140.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart before deletion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234287164-66362c83-b53e-49b0-8dbe-c5b3d38cee1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart after deleting &quot;Greenlights Hardcover&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234287476-c4576539-2dda-48d0-83ac-69f5dc918af1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/69519007/234287677-a412f66c-9af9-42d5-aad6-5ac4c9192d71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing cart (all items deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>For each delete request, that particular item is deleted from the cart table,<br>i.e, a delete command is issued where userid=current user and item_id= respective item<br>id. While clearing a cart, all items associated with that particular user is<br>deleted from the cart table.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/CK-ghub/IS601-004/pull/61">https://github.com/CK-ghub/IS601-004/pull/61</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Frontend work was tedious, especially aligning the footer and CSS styles was quite<br>challenging. I solved this by adding a few custom templates, hardcoding a couple<br>of values by trial and error, and playing around CSS styles to ensure<br>that they retained their respective positions in the page. Apart from the frontend<br>work, I did not face any major issues after Milestone1. There was quite<br>a lot of learning this time, and the tasks listed in this milestone<br>along with base templates helped me create a full-stack web application.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-kc664-project-prod.herokuapp.com/login">https://is601-kc664-project-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/kc664" target="_blank">Grading</a></td></tr></table>