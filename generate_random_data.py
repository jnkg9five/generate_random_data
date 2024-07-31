from faker import Faker
import json

def gen_rand_data(fake, size):
    for i in range(size):
        #generate random data using faker lib
        name = fake.name()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()
        job = fake.job()
        company = fake.company()

        #set header for dataset index
        print("Dataset Index:", i)

        #print random generated data to output
        print("Name:", name)
        print("Address:", address)
        print("Phone Number:", phone_number)
        print("Email:", email)
        print("Job:", job)
        print("Company:", company)

def main():
    #make faker instance 
    fake = Faker()

    #take in value of data set size
    size = int(input("What is the data set size to be generated? "))
    
    random_datas = gen_rand_data(fake, size)

    #print generated data in JSON
    print(json.dumps(random_datas, indent=4))

if __name__ == "__main__":
    main()