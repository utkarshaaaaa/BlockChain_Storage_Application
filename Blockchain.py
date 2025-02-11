
import random
from Block import Block


class Blockchain:
  
    difficulty = 3
    def __init__(self):
        self.pending = [] 
        self.chain = [] 
        genesis_block = Block(0, [], "0") 
        genesis_block.hash = genesis_block.generate_hash() 
        self.chain.append(genesis_block) 

    
    
    def add_block(self, block, hashl):
        prev_hash = self.last_block().hash
        
        if (prev_hash == block.prev_hash and self.is_valid(block, hashl)):
            block.hash = hashl
            self.chain.append(block)
            return True
        else:
            return False


    
    def mine(self):
        if(len(self.pending) > 0): 
            last_block = self.last_block() 
            new_block = Block(last_block.index + 1,self.pending,last_block.hash)

            
            hashl = self.p_o_w(new_block)
           
            self.add_block(new_block, hashl)
            
            self.pending = []
            
            return new_block.index
        else:
            return False

    
    def p_o_w(self, block):
        block.nonce = 0
        get_hash = block.generate_hash() 
        while not get_hash.startswith("0" * Blockchain.difficulty): 
            block.nonce = random.randint(0,99999999) 
            get_hash = block.generate_hash() 
        return get_hash
  
    def p_o_w_2(self, block):
        block.nonce = 0
        get_hash = block.generate_hash()    
        while not get_hash.startswith("0" * Blockchain.difficulty): 
            block.nonce += 1   
            get_hash = block.generate_hash()
        return get_hash

   
    def add_pending(self, transaction):
        self.pending.append(transaction)
        
   
    def check_chain_validity(this, chain):
        result = True
        prev_hash = "0"
       
        for block in chain:
            block_hash = block.hash 
            if this.is_valid(block, block.hash) and prev_hash == block.prev_hash:
                block.hash = block_hash 
                prev_hash = block_hash 
            else:
                result = False
        return result

    
    def is_valid(cls, block, block_hash):

        if(block_hash.startswith("0" * Blockchain.difficulty)):
            if(block.generate_hash() == block_hash):
                return True
            else:
                return False
        
        else:
            return False


    def last_block(self):
        return self.chain[-1]
