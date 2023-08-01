CREATE TABLE 
    IS601_S_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        first_name varchar(50),
        last_name varchar(50),
        total_price int,
        number_of_items int,
        user_id int,
        address varchar(200),
        payment_method varchar(30),
        money_received float,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )