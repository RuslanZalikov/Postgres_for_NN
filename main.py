import psycopg2
from config import *

def get_trb():

    count = 0

    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )
        print("Мы внутри OK")
        count += 1

        with connection.cursor() as cur:
            cur.execute(
                """
                select s3_path, trb
                from transcribations join audio_fragment
                on transcribations.fragment_id = audio_fragment.id
                where transcribations.valid is True;
                """
            )
            data = cur.fetchall()
        print("Без ошибок OK")
        count += 1


    except Exception as e:
        print("Badabum beda ERROR", e)

    finally:
        if connection:
            connection.close()
            print("Закрылись OK")
            count += 1
            print(f"{count}/3")
            return data

if __name__ == "__main__":
    print(get_trb())