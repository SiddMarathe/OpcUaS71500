import RTC as today
class text_edit:
    def __init__(self, path, name, data=None):
        self.f_n=name
        self.f_p=path
        self.data=data
    #WRITE
    def txt_g(self):
        path=self.f_p+self.f_n+'.txt'
        mode='w+'
        text=input("Enter your text:\n")
        try:
            with open(path,mode) as file:
                amount_written=file.write(text)
        finally:
            if len(text)==amount_written :
                print('File has been generated.')
                return 0
            else:
                print('File error.')

    #'/storage/emulated/0/'
    #READ
    def txt_r(self):
        path=self.f_p+self.f_n+'.txt'
        try:
            mode='r'
            with open(path,mode) as file:
                print('File: '+file.read())
        except:
            print('File error.')
            
            
            
    #Append
    def txt_a(self):
        path=self.f_p+self.f_n+'.txt'
        try:
            mode='a'
            with open(path,mode) as file:
                file.write(str(input('Enter the text:\n')+'\n'))
                mode='r'
            with open(path,mode) as file:
                 print('File: '+file.read())
        except:
             print('File error.')
        
    def txt_log(self,data):
        path='{}{}_{}{}'.format(self.f_p,self.f_n,today.RTC().date(),'.txt')
        try:
            
            mode='a'
            with open(path,mode) as file:
                file.write('\n'+data)
            #     mode='r'
            # with open(path,mode) as file:
            #      print('File: '+file.read())
        except:
            print('File does not exist.')
            mode='w+'
            try:
                with open(path,mode) as file:
                    file.write('\n'+data)
            except:
                print('File Error.')
                pass

if __name__ == "__main__":
    print(today.RTC().date())    
    txt_jalvis=text_edit(input('Enter file path: '),input('Enter file name: '))
    txt_jalvis.txt_g()
    txt_jalvis.txt_r()