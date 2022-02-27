trigger Error_Messages on Salary_Chnages__c (before insert, before delete)
{
Set<String> Term_Dates = new Set<String>();
for(Salary_Chnages__c obj: [Select Term_Date__c from Salary_Chnages__c])
Term_Dates.add(obj.Term_Date__c);
for(Salary_Chnages__c obj: Trigger.new)
{
if(!Term_Dates.contains(obj.Term_Date__c))
{
Term_Dates.add(obj.Term_Date__c);
}
else
{
obj.Term_Date__c.addError('For a given effective date only one salary account should be there');
}
}
}





trigger update_salary on Salary_Chnages__c (after insert) {
    List<Employees__c>obj2List = new List<Employees__c>();
    for(Salary_Chnages__c obj1:Trigger.new)
    { 
    Employees__c emp=new Employees__c();
   if( emp.Name==Salary_Chnages__c.Empployee.Name)
   {
   	if(Date.daysBetween(Salary_Chnages__c.Effective_Date__c,Salary_Chnages__c.Term_Date__c))
	emp.Current_Salary=obj1.New_Salary__C)); 
	}

    }  

}
