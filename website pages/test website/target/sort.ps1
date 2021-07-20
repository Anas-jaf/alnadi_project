#this powershell file  will collect all the text files in one file 


# i managed to sort the files by :-
#1-putting the folder names in array 


$homeDir = "D:\????? ???? ???????\website pages\test website\target"
cd $homeDir
$string = @(
"10_الارقام",
"11_مقاطع عامة اثنين",
"12_اساسي المرحلة الثانية",
"13_الرموز",
"14_مقاطع عامة الجزء الثالث",
"15_متقدم الجزء الاول",
"16_رموز اكثر",
"17_كلمات مخادعة الجزء الثاني",
"18_ متقدم الجزء الثالث",
"19_متقدم الجزء الثاني",
"1_سطر المركز",
"20_متقدم المرحلة الرابعة",
"21_متقدم المرحلة الخامسة",
"22_متقدم المرحلة السادسة",
"23_متقدم المرحلة السابعة",
"24_متقدم المرحلة الثامنة",
"25_متقدم المرحلة التاسعة",
"2_السطر العلوي",
"3_السطر السفلي",
"4_اساسي",
"5_كلمات مخادعة",
"6_الحركات",
"7_مقاطع عامة واحد",
"8_ اساسي المرحلة  الاولى",
"9_كلمات مخادعة الجزء الاول")

$myobjecttosort=@()

#2-running a function that i found in the internet to sort the array https://social.technet.microsoft.com/Forums/windowsserver/en-US/76a3de17-0888-4608-90e2-a32b3dde16be/sort-object-with-numbers-after-a-string?forum=winserverpowershell
 
$string | ForEach{
    $myobjecttosort+=New-Object PSObject -Property @{    
    'String'=$_
    'Numeric'=[int]([regex]::Match($_,'\d+')).Value
  }
 }
 

$myobjecttosort | Sort-Object Numeric | Select Numeric,String | Format-Table -AutoSize

$newObject = $myobjecttosort | Sort-Object Numeric

$num = 0
foreach ($item in $newObject) {
 $num++
#  $collection = $newObject[$num].String
 try { 
    #  Get-Content "$($newObject[$num].String)\*.txt" "`n" | Set-Content JSON.txt 
    Get-Content "$($newObject[$num].String)\*.txt" | add-Content JSON.txt
        # $i = 0
        # foreach ($item in $collection) {
        #     $i++
        #     Get-Content "$($newObject[$i].String)\$item`.txt" -Tail 1234 | Set-Content JSON.txt
        # }

    }
# i learned to nest object property from  "$($newObject[$num].String)\*.txt" from this stack page https://stackoverflow.com/a/1145822/13312280
 catch {
     "an error occurred"
     Write-Host $_ }
finally {
    add-content JSON.txt -value "`n"
    echo "copied all the files from " $newObject[$num].String
    Read-Host -Prompt "Press any key to continue"}

}

# inspired from this stack page
# https://stackoverflow.com/questions/8749929/how-do-i-concatenate-two-text-files-in-powershell
# Get-Content '<fileDirictory>\*.txt'| Set-Content JSON.txt



