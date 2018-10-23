class copybinaryfile:
    def __init__(self,path):
        print("Enter Path:    ")
        self.path = path
        f1=open(path,'rb')
        c1=f1.read()
        outpath=path+"out"
        outf1=open(outpath,'wb')
        outf1.write(c1)
        f1.close()
        
  
