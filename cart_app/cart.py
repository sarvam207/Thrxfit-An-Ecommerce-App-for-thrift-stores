class Cart():
    def __init__(self, request):
        
        self.session = request.session
        # existing user cart
        user_cart = self.session.get('session_key')
        # new user cart
        if 'session_key' not in request.session:
            user_cart = self.session['session_key'] = {}
        
        self.user_cart = user_cart