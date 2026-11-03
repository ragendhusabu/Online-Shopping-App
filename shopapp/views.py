
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.

class About(View):
    def get(self,request):
        data = {
            "Website_Name": "ShopEasy",
            "Description": "An online shopping platform for everyday products.",
            "Email": "shopeasy@gmail.com",
            "Contact": 9876543210,
            "Website": "https://www.shopeasy.com",
            "Location": "Kochi, Kerala"
        }

        return JsonResponse(data)


class ProductView(View):
    def get(self,request):
        products = [
            {
                "id": 1,
                "product_name": "Wireless Headphones",
                "category": "Electronics",
                "brand": "boAt",
                "price": 1999,
                "description": "Wireless headphones with clear sound and long battery life.",
                "stock": 25,
                "rating": 4.5,
                "available": True
            },
            {
                "id": 2,
                "product_name": "Cotton T-Shirt",
                "category": "Fashion",
                "brand": "Roadster",
                "price": 799,
                "description": "Comfortable cotton T-shirt for everyday use.",
                "stock": 40,
                "rating": 4.2,
                "available": True
            },
            {
                "id": 3,
                "product_name": "Smart Watch",
                "category": "Electronics",
                "brand": "Noise",
                "price": 2499,
                "description": "Smart watch with fitness tracking and notification features.",
                "stock": 15,
                "rating": 4.6,
                "available": True
            },
            {
                "id": 4,
                "product_name": "Travel Backpack",
                "category": "Accessories",
                "brand": "Skybags",
                "price": 1499,
                "description": "Spacious backpack suitable for travel and daily use.",
                "stock": 20,
                "rating": 4.3,
                "available": True
            },
            {
                "id": 5,
                "product_name": "Running Shoes",
                "category": "Footwear",
                "brand": "Puma",
                "price": 2999,
                "description": "Lightweight running shoes designed for comfort.",
                "stock": 0,
                "rating": 4.4,
                "available": False
            }
        ]

        return JsonResponse(products,safe=False)


class CategoryView(View):
    def get(self,request):
        categories = [
            {
                "id": 1,
                "category_name": "Electronics",
                "description": "Electronic gadgets and accessories.",
                "total_products": 50
            },
            {
                "id": 2,
                "category_name": "Fashion",
                "description": "Clothing and fashion products.",
                "total_products": 75
            },
            {
                "id": 3,
                "category_name": "Footwear",
                "description": "Shoes, sandals and slippers.",
                "total_products": 30
            },
            {
                "id": 4,
                "category_name": "Accessories",
                "description": "Bags, watches and other accessories.",
                "total_products": 40
            }
        ]

        return JsonResponse(categories,safe=False)


class CustomerView(View):
    def get(self,request):
        customers = [
            {
                "id": 1,
                "customer_name": "Arun Kumar",
                "email": "arun@gmail.com",
                "phone": 9876543211,
                "city": "Kochi",
                "membership": "Gold"
            },
            {
                "id": 2,
                "customer_name": "Meera Thomas",
                "email": "meera@gmail.com",
                "phone": 9876543212,
                "city": "Kozhikode",
                "membership": "Silver"
            },
            {
                "id": 3,
                "customer_name": "Rahul Raj",
                "email": "rahul@gmail.com",
                "phone": 9876543213,
                "city": "Trivandrum",
                "membership": "Regular"
            }
        ]

        return JsonResponse(customers,safe=False)


class OrderView(View):
    def get(self,request):
        orders = [
            {
                "id": 1,
                "customer_id": 1,
                "customer_name": "Arun Kumar",
                "product_name": "Wireless Headphones",
                "quantity": 2,
                "total_amount": 3998,
                "order_date": "2026-11-01",
                "order_status": "Delivered"
            },
            {
                "id": 2,
                "customer_id": 2,
                "customer_name": "Meera Thomas",
                "product_name": "Cotton T-Shirt",
                "quantity": 1,
                "total_amount": 799,
                "order_date": "2026-11-02",
                "order_status": "Shipped"
            },
            {
                "id": 3,
                "customer_id": 3,
                "customer_name": "Rahul Raj",
                "product_name": "Smart Watch",
                "quantity": 1,
                "total_amount": 2499,
                "order_date": "2026-11-03",
                "order_status": "Processing"
            }
        ]

        return JsonResponse(orders,safe=False)


class PaymentView(View):
    def get(self,request):
        payments = [
            {
                "id": 1,
                "order_id": 1,
                "payment_method": "UPI",
                "amount": 3998,
                "payment_date": "2026-11-01",
                "payment_status": "Successful"
            },
            {
                "id": 2,
                "order_id": 2,
                "payment_method": "Credit Card",
                "amount": 799,
                "payment_date": "2026-11-02",
                "payment_status": "Successful"
            },
            {
                "id": 3,
                "order_id": 3,
                "payment_method": "Cash on Delivery",
                "amount": 2499,
                "payment_date": "2026-11-03",
                "payment_status": "Pending"
            }
        ]

        return JsonResponse(payments,safe=False)


class OfferView(View):
    def get(self,request):
        offers = [
            {
                "id": 1,
                "offer_name": "Festival Sale",
                "discount_percentage": 20,
                "description": "Get 20% discount on selected products.",
                "valid_until": "2026-12-31",
                "active": True
            },
            {
                "id": 2,
                "offer_name": "New Customer Offer",
                "discount_percentage": 15,
                "description": "Special discount for first-time customers.",
                "valid_until": "2026-12-15",
                "active": True
            },
            {
                "id": 3,
                "offer_name": "Electronics Sale",
                "discount_percentage": 10,
                "description": "Get 10% discount on selected electronics.",
                "valid_until": "2026-12-20",
                "active": True
            }
        ]

        return JsonResponse(offers,safe=False)
