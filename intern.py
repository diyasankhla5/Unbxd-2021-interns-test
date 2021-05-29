import requests
import json
import csv
response=requests.get("https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*");
join_response=response.json();
number_of_products=join_response["response"]["numberOfProducts"];
#print(number_of_products);
for i in range(0,int(number_of_products/100)):
    response=requests.get("https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=100&start="+str(i));
    join_response=response.json();

    product_data=join_response["response"]["products"];
    for data in product_data:
        for (key,item) in data.items():
            if(isinstance(item,list)):
                if(key=="unbxd_color_for_category" or key=="colorSwatch" or key=="test_colors" or key=="unbxd_color_mapping"):
                    #print("heyyy");
                    my_list=[i.split('::', 1)[0] for i in item];
                # print(my_list);
                    item=my_list;
                    



                converted_set=set({str(element) for element in item})
            
                converted_list=list(converted_set);

                joined_string=",".join(converted_list);
                if(joined_string=="False"):
                    joined_string="NO";
                if(joined_string=="true"):
                    joined_string="YES";
                data[key]=joined_string;

        with open('Unbxd-2021-interns test Diya Sankhla.csv', 'a+', newline = '') as csvfile:
            my_writer = csv.writer(csvfile, delimiter = ' ')
            my_writer.writerow(data.values());  



                
            
        
    




