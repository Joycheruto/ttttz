/*#include<stdio.h>
int main()
{
    int principle,n;
    float rate,simple_intrest;
    principle = 20000;
    n = 3;
    rate = 3.5;
    

    //printf("|\nenter the valesof principle,n,rate");
    //scanf ("%d%d%f",&principle,&n,&rate);

    simple_intrest=principle*rate*n/100;
    printf("\nthe simple intrest is %.3f",simple_intrest);

    return 0;

}
   

#include<stdio.h>
int main()
{
    float basic_salary;
    float allowance_1,allowance_2,gross_salary;

    printf("\n Enter the basic salary,allowance1,allowance2");
    scanf("%f%f%f",&basic_salary,&allowance_1,&allowance_2);

    gross_salary = basic_salary+allowance_1+allowance_2;
    printf("\n the gross salary is : %f",gross_salary);
    return 0;
} 

#include<stdio.h>
int main(){
    int math,eng,kis,chem,bio,aggregate;
    float percentage;

    printf("\nenter the marks,math,eng,kis,chem,bio");
    scanf("%d%d%d%d%d",&math,&eng,&kis,&chem,&bio);

    aggregate=math+eng+kis+chem+bio;
    percentage = ((float)aggregate /500) *100;
    printf("\n the aggregate is:%d",aggregate);
    printf("\n the percentage of the student is : %f",percentage);
    return 0;

}
    
    #include<stdio.h>
    int main (){

        int num ;

        printf("\n Enter the num");
        scanf("%d",&num);

        if(num%2==0){
            printf("\n yeah,its an even number!!");
        }else{
            printf("\n ts an odd number");
        }
        return 0;
      }
    */


#include<stdio.h>
int main(){

    int cash_price,sell_price,profit,loss;
    

    printf("\n ENTER THE CASH PRICE ");
    scanf("%d",&cash_price);

    printf("\n ENTER THE SELL PRICE ");
    scanf("%d",&sell_price);

    profit = sell_price-cash_price;
    loss =cash_price-sell_price;

    if(sell_price>cash_price){
        printf("\n a profit has been made of :%d",profit);

    }else{
        printf("\n a loss has been made of: %d",loss);
    }
    return 0;
}
