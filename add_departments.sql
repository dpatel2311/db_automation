CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);

INSERT INTO departments (department_name, location) VALUES
('HR', 'kitchener'),
('Engineering', 'waterloo');
('IT', 'cambridge');

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

ALTER TABLE departments
MODIFY COLUMN location VARCHAR(500);

DELETE FROM departments WHERE department_id = 2;
