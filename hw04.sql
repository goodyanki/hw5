use homework04;
CREATE TABLE categories (
    category_ID INT AUTO_INCREMENT,
    category VARCHAR(20) NOT NULL,
    PRIMARY KEY (category_ID)
);
CREATE TABLE Expenses (
    expense_ID INT AUTO_INCREMENT,
    category_ID INT NOT NULL,
    expense_date DATETIME NOT NULL,
    expense VARCHAR(30) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    notes VARCHAR(30),
    PRIMARY KEY (expense_ID),
    FOREIGN KEY (category_ID) REFERENCES categories(category_ID)
);