def get_customer_metrics(*, data, from_, to, min_total_spend=None):
    customer = {}
    
    for order in data:
        order_date = order.get("orderDate")
        
        if order_date < from_ or order_order > to:
            continue
            
        customer_id = order.get("customerId")
        line_items = order.get("lineitems", [])

        order_total = sum(
            item.get("quantity",0) * item.get("uniPrice", 0)
            for item in line_items
        )
        
        if customer_id not in customers:
            customers[customer_id] = {
                "customerId": customer_id
                "orderCount": 0,
                "totalSpend": 0,
            }
            
        customer[customer_id]["orderCount"] += 1
        customer[customer_id]["totalSpend"] += order_total

    results = []

    for customer in customers.values():
        if min_total_spend is not None and customer["totalSpend"] < min_total_spend:
            continue
            
        customer["avgOrderValue"] = customer["totalSpennd"] / customer["orderCount"]
        results.append(customer)
        
    results.sort(key=lambda x: x["customerId"])
        
    return {"results": results}
