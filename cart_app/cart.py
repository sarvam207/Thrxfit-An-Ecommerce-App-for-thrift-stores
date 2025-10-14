from store_app.models import Product
from decimal import Decimal



class Cart():
    
    def __init__(self, request):
        
        self.session = request.session
        # existing user cart
        user_cart = self.session.get('session_key')
        # new user cart
        if 'session_key' not in request.session:
            user_cart = self.session['session_key'] = {}
        
        self.user_cart = user_cart
        
        
        
    
    def add(self, product, quantity):
        product_id = str(product.id) # converting to string as session only accepts string keys
        
        if product_id in self.user_cart:
            self.user_cart[product_id]['quantity'] = quantity
        else:
            self.user_cart[product_id] = {'price': str(product.price), 'quantity': quantity, 'image': product.image.url, 'name': product.name}
        
        self.session.modified = True # to make sure session is saved
        
        
        
        
        
    def __len__(self):
        return sum(item['quantity'] for item in self.user_cart.values())





    def unique_count(self):
        """Return number of unique products in the cart."""
        return len(self.user_cart.keys())
    
    
    
    
    
    def __iter__(self):
        product_ids = self.user_cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        import copy
        cart = copy.deepcopy(self.user_cart)
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
            
            
        
            
    def get_total(self):
        return sum(float(item['price']) * item['quantity'] for item in self.user_cart.values())
    
    
    
    
    
    
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.user_cart:
            del self.user_cart[product_id]
            self.session.modified = True
            
    def update(self, product, qty):

        product_id = str(product)
        product_quantity = qty

        if product_id in self.user_cart:

            self.user_cart[product_id]['qty'] = product_quantity

        self.session.modified = True