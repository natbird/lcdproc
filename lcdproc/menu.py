class Menu(object):
	
	    """ LCDproc Menu Object """
	    
	    def __init__(self, server, ref, item, text, parent="\"\""):
	    
	    	""" Constructor """
	    	
	    	self.server = server
	    	self.ref = ref
	    	self.name = ref
	    	self.item = item
	    	self.text = text
	    	self.parent = parent
	    	self.hidden = None
	    	
	    	self.server.request("menu_add_item %s %s %s %s" % (self.parent, self.ref, self.item, self.text))
	    	
	    	
	    def set_text(self, text):
	        
	        """ Set Text """
	        
	        self.text = text
	        self.server.request("menu_set_item %s %s -text %s" % (self.parent, self.ref, self.text))
	    
	    
	    def set_hidden(self, state):
	        
	        """ Set Visibility of Item """
	        
	        if state in ["true", "false"]:
	            self.hidden = state
	            self.server.request("menu_set_item %s %s -is_hidden %s" % (self.parent, self.ref, self.hidden))
	    
	    
	    def set_next(self, next_id):
	        
	        """ Set Next Item """
	        
	        self.next = next
	        self.server.request("menu_set_item %s %s -next %s" % (self.parent, self.ref, self.next))
	    
	    
	    def set_previous(self, predecessor_id):
	        
	        """ Set Next Item """
	        
	        self.prev = prev
	        self.server.request("menu_set_item %s %s -prev %s" % (self.parent, self.ref, self.prev))
	    
	    
	    def set_value(self, value):
	        
	        """ Set Item Value """
	        
	        self.value = value
	        self.server.request("menu_set_item %s %s -value %s" % (self.parent, self.ref, self.value))
