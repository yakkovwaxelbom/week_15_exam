from typing import List, Dict, Any

def execution(func):
    def wrapper(con):
        q = func()

        cnx = con.cursor()
        cnx.execute(q)
        results = cnx.fetchall()
        cnx.close()

        return results
    
    return wrapper

@execution
def get_customers_by_credit_limit_range():

    q = '''select customerName, creditLimit
        from customers
        where creditLimit < 10000 or 100000 < creditLimit;'''

    return q

@execution
def get_orders_with_null_comments():
    
    q = """select orderNumber, comments
        from orders
        where comments is null
        order by orderDate;"""
    
    return q

@execution
def get_first_5_customers():
    q = """"select customerName, contactFirstName, contactLastName
        from customers
        order by contactLastName 
        limit 5;"""
    
    return q

@execution
def get_payments_total_and_average():

    q = """"select sum(amount) as total_sum, avg(amount) as average_sum, max(amount) as max_sum, min(amount) as min_sum
        from payments;"""

    return q

@execution
def get_employees_with_office_phone():

    q = """select firstName, lastName, phone
        from employees natural join offices;"""
    
    return q

@execution
def get_customers_with_shipping_dates():
    
    q = """select c.customerName , o.orderDate 
        from customers c left join orders o on c.customerNumber = o.customerNumber;"""

    return q

@execution
def get_customer_quantity_per_order():
    
    q = """with temp (orderNumber, total_quantity) 
        as (select orderNumber, sum(quantityOrdered)
            from orderdetails
            group by orderNumber)
            
        select c.customerName, t.orderNumber, t.total_quantity 
        from customers c natural join orders o natural join temp t
        order by c.customerName;"""

    return q

@execution
def get_customers_payments_by_lastname_pattern():
    
    q = """select c.customerName, concat(c.contactFirstName, ' ', c.contactLastName) as contactName, sum(amount) as total_payments
        from customers c join payments p
        where c.contactFirstName like '%Mu%' or c.contactFirstName like '%ly%'
        group by c.customerName, contactName
        order by total_payments;"""
    
    return q
