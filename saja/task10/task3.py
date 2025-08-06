customers = (("Alex", "VIP"), ("Bob", "Regular"),("Sarah", "Regular"),
    ("Maria", "VIP"), ("Mike", "Regular"))

vip_queue = []
regular_queue = []

for customer in customers:
    name, cust_type = customer
    if cust_type == "VIP":
        vip_queue.append(name)
    else:
        regular_queue.append(name)

serving_order = vip_queue + regular_queue

print("Serving Order:")
for name in serving_order:
    print("-", name)