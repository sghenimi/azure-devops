from decouple import config
def main():
  
  print(f'Env={config(ENVIRONMENT)}')
if __name__ == '__main__':
  main()
