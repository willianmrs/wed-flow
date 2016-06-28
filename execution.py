import schedule
import time



if __name__ == "__main__":


# cria as filas

schedule.every(10).second.do(job)



while True:
    schedule.run_pending()
    time.sleep(1)