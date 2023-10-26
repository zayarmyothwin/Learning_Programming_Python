# programming-basic-python created on Oct 2023
## Saturngod ရဲ့ Programming Basic စာအုပ်ဖတ်ပီးထုတ်ထားတဲ့ note များ
-------------------------------------------------------------
## အခန်း (၁) Programming ဆိုတာ
### Sequential
Programming မှာcodeတွေကတစ်ကြောင်းစီအလုပ်လုပ်တယ်။
### Variable
Variable ဆိုတာက data တွေကိုခဏတာ memory ပေါ်မှာသိမ်းထားပေးတဲ့နေရာပါ။ variable ကိုနာမည်ပေးဖို့လိုတယ်။ variable အမျိုးအစားလဲသတ်မှတ်ပေးဖို့လိုပါတယ်။
```python
counter=100 # An integer assignment
miles=100.0 # A floating point
name="John" # A String
boolean=True # Boolean value True and False only
```
### Bit and Stroage Data on Memory
Variable က memory ပေါ်မှာနေရာယူပီးခဏသိမ်းတယ်။Program ပိတ်လိုက်တဲ့အခါမှာ memory ပေါ်ကနေလည်းရှင်းလင်းလိုက်တယ်။ Computer မှာ 0 နဲ့ 1 ဘဲရှိတယ်။အဲ့ဒါကိုbitလို့ခေါ်တယ်။
* 8 bit ကို 1 byte။ 8 bit က binary system အရ 00000000 ကနေ 11111111 ထိရှိတယ်။
* binary value 11111111 ကို decimal ပြောင်း 255 ရလာပါတယ်။ 8 bit မှာအများဆုံးသိမ်းနိုင်တဲ့တန်ဖိုး။
* Integer ဟာ 32 bit ရှိပါတယ်။ Integer တန်ဖိုးမှာ unsigned နဲ့ signed ဆိုပီးရှိတယ်။ Unsign ဟာအပေါင်းကိန်းတွေဘဲဖစ်တဲ့အတွက် 32 bit အပြည့်အသုံးပြုနိုင်တယ်။ Signed ကတော့ +/- ပါတဲ့အတွက်ကြောင့် 31 bit ဘဲအသုံးပြုနိုင်တယ်။ 1 bit ကို အပေါင်းလားအနုတ်လားဆုံးဖြတ်ဖို့အတွက်ပေးရတယ်။

### Operators
Operators ဆိုတာကတော့ပေါင်းနှုတ်မြှောက်စားပါ။ Programming မှာ
* အပေါင်း +
* အနှုတ် -
* အမြှောက် * 
* အစား /
* အကြွင်း % 

## အခန်း (၂) Programming
### Pseudo code
Pseudo code ဆိုတာအတုအယောက်code ပုံမှန် english လိုဘဲရေးထားတာ။ Input, output, processing တွေအတွက်အောက်ပါ keyword တွေကိုအသုံးပြူတယ်။
* Input: READ, OBTAIN, GET
* Output: PRINT, DISPLAY, SHOW
* Compute: COMPUTE, CALCULATE, DETERMINE
* Initialize: SET, INIT
* Add one: INCREMENT, INCREASE, DECREMENT, DECREASE

### Flow Chart
Flow chart ဆိုတာကဘာပြီးရင်ဘာလုပ်မယ်ဆိုတာကို အဆင့်ဆင့်ပုံတွေနဲ့ဆွဲပြထားတာပါ။
#### Terminal
![Terminal](/image-note/terminal.png)
* Flow chart အစ သို့မဟုတ် အဆုံး စသည့်နေရာတွေမှာအသုံးပြုပါတယ်။
* အစကို start begin
![Start,Begin](/image-note/start-begin.png)
* အဆုံးကိုတော့ End, Exit, Return တွေကိုအသုံးပြုပါတယ်။
![End](/image-note/end.png)

#### Line with arrows
* တစ်ခုကနေနောက်တစ်ခုကိုသွားဖို့ညွှန်ပြထားတာပါ။ဒါအဆင့်ပြီးရင်ဘယ်ကိုသွားမလဲဆိုတာကိုညွှန်ပြတာပါ။
![arrow](/image-note/arrow.png)

#### Rectangle
* Flowchart မှာစတုဂံတွေကို process, task, action, operationစသည့်အတွက်အသုံးပြုပါတယ်။စတုဂံပုံဟာ action တခုခုလုပ်ဖို့တခုခုပြီးမြောက်ဖို့အတွက်ညွှန်ပြထားပါတယ်။
![Rectangle](/image-note/rectangle.png)

#### Decision
![Decision](/image-note/decision.png)
* user ကိုမေးခွန်းမေးပြီးတော့အဖြေအပေါ်မူတည်ပြီးအလုပ်လုပ်စေချင်တဲ့အခါမှာ decision ကိုအသုံးပြုရပါတယ်။ input တစ်ခုဝင်ပြီးတော့ output မှာ Yes, No ဖြစ်ပါတယ်။ဒါဖြစ်ခဲ့ရင်ဒါလုပ် မဟုတ်ခဲ့ရင်ဘာလုပ်စသည်အတွက်အသုံးပြုနိုင်ပါတယ်။
![decision yesno](/image-note/yesno.png)

#### Circle
* Flowchart ကအရမ်းရှည်သွားရင်သီးသန့်ဆွဲဖို့အတွက် circle ကိုအသုံးပြုပါတယ်။ flowchart တစ်ခုနဲ့တစ်ခုကို connect လုပ်ထားတယ်ဆိုတာကိုဖော်ပြထားသည့်သဘောပါ။ Circle အတွင်းမှာနာမည်ပါဝင်ပါတယ်။
![Circle](/image-note/circle.png)

#### Input/Output
* User ဆီကနေ Data တွေကိုလက်ခံတော့မယ်ဆိုရင်တော့အနားပြိုင်စတုဂံကိုအသုံးပြုပါတယ်။
![Input/output](/image-note/input.png)

### Flowchart with codes
Programming ရဲ့အစ Hello World

#### Pseudo code နဲ့ဆိုရင်
print("Hello World")

#### Flow chart နဲ့ဆိုရင်
![Hello World](/image-note/helloworld.png)

#### Python နဲ့ဆိုရင်
print("Hello World")

### Condition
ဒါမှမဟုတ်ရင်ဒါလုပ်မယ်စသည်ဖြင့်အခြေအနေကိုစစ်သည့်အရာတွေအတွက် if,switch စတဲ့ syntax ကိုအသုံးပြုရပါတယ်။ Python မှာတော့ switch ကို support မလုပ်ဘူး။

### Looping
Looping ဆိုတာကတော့ထပ်ခါထပ်ခါလုပ်တဲ့အခါတွေမှာအသုံးပြုပါတယ်။ Looping အမျိုးအစား ၃ မျိုးရှိပါတယ်။
* For Loop
* While Loop
* Do While Loop
Python မှာတော့ Do While Loop ကို support မလုပ်ပါဘူး။

#### For Loop
အကြိမ်အရေအတွက်အတိအကျရှိတယ်ဆိုရင်တော့ For Loop ကိုအသုံးပြုနိုင်ပါတယ်။ဘယ်ကနေစပြီးဘယ်အထိသိတယ်ဆိုရင်တော့ For Loop ကိုအသုံးပြနိုင်ပါတယ်။

#### While Loop
အကြိမ်အရေအတွက်ကိုမသိဘူး ဒါမှမဟုတ် condition တစ်ခုခုကိုထားပြီးတော့ loop လုပ်မလားမလုပ်ဘူးလားဆိုတာကိုသိချင်တဲ့အခါမှာတော့ While Loop ကိုအသုံးပြုရပါတယ်။

#### Do While Loop
Do While Loop က While Loop လိုပါဘဲ။ဒါပေမဲ့ အနည်းဆုံးတကြိမ်အလုပ်လုပ်တယ်။

### Array
Array ဆိုတာက variable တွေအများကြီးကိုသိမ်းထားတဲ့ variable တစ်ခု။ Array က variable တွေကိုအခန်းနဲ့သိမ်းပါတယ်။

#### Immutable and Mutable
Array မှာ ၂မျိုးရှိတယ်။မပြောင်းလို့ရတဲ့ Array(immutable) နဲ့ ပြောင်းလဲလို့ရတဲ့ Array(mutable) Type ၂ခုရှိပါတယ်။ Python မှာကတော့ tupe(immutable) နဲ့ list(mutable) ဆိုပြီး ၂မျိုးရှိတယ်။ tuple ကိုလက်သည်းကွင်းနဲ့ ရေးပြီးတော့ list ကိုတော့လေးထောင့်ကွင်းနဲ့ရေးပါတယ်။
```python
t=(1,2,3) #immutable
l=[1,2,3] #mutable
```
### Function
Code တွေထပ်နေရင် သို့မဟုတ် ပိုပြီးတော့အဓိပ္ပာယ်ပြည့်စုံအောင် function ခွဲရေးပါတယ်။

## အခန်း(၃) Object Oriented
Object Oriented ဆိုတာကတော့ programming ကိုရေးသားရာမှာသက်ဆိုင်ရာအစုလိုက်ခွဲထုတ်ပြီးရေးသားထားတာပါ။ ဉပမာ - ကားတစ်စီးကို object လို့သတ်မှတ်လိုက်။သူ့မှာ properties တွေ function တွေရှိမယ်။ Properties တွေကတော့ ဘီး ၄ခုရှိမယ်။ Function တွေကတော့ ရှေ့သွားမယ်၊နောက်သွားမယ်၊ဘယ်ကွေ့၊ညာကွေ့တွေပါမယ်။ Programming မှာဖန်တီးတဲ့အခါမှာလည်း Object ကိုဖန်တီးတယ်။ပြီးရင် properties တွေ function တွေကိုသက်ဆိုင်ရာ Object မှာထည့်သွင်းပါတယ်။

### Classes
Class ဆိုတာကတော့ Object တစ်ခုဖန်တီးဖို့အတွက် user-defiend လုပ်ထားတာပါ။ Class ထဲမှာ attributes, class variables, method စတာတွေပါဝင်ပါတယ်။

#### Defining a Class
Python မှာ class ကိုဖန်တီးတော့မယ်ဆိုရင်
```python
class ClassName:
```
ClassName ကနှစ်သက်ရာ class နာမည်ပါ။ဉပမာ-
```python
class animal:
```
animal ဆိုတဲ့ class ကိုတည်ဆောက်ပီးပီပြီးရင် class ထဲမှာပါဝင်မယ့် variable ကိုသတ်မှတ်ပါမယ်။ animal ဖြစ်တဲ့အတွက်ကြောင့်ခြေထောက် ၄ချောင်းဖစ်နိုင်သလို၂ချောင်းတည်းရှိတဲ့ animal လည်းဖြစ်နိုင်တယ်။ဒါကြောင့်
```python
class animal:
    number_of_legs=0
```
### Instances
Class ကြီးသက်သက်ဆိုရင်တော့ class တစ်ခုကိုဖန်တီးထားတာဘဲရှိပါတယ်။ class ကိုအသုံးပြုချင်ရင်တော့ instance တစ်ခုကိုတည်ဆောက်ရပါတယ်။တည်ဆောက်ပီးသား instance ကို variable ထဲမှာသိမ်းရပါတယ်။ class ထဲက variable တွေကိုခေါ်ယူအသုံးပြုလိုရင်တော့ instance ဆောက်ထားတဲ့ variable ထဲကနေတဆင့်ခေါ်ယူအသုံးပြုနိုင်ပါတယ်။
```python
class animal:
    number_of_legs=0
dog=animal()
```
dog variable က animal object တစ်ခုဖြစ်သွားပါပီ။Animal ထဲက variable ကိုခေါ်ယူအသုံးပြုလိုရင်။
```python
dog.number_of_legs
```
Variable ကိုအသုံးပြုကြည့်မယ်
```python
#code here
```

### Function in Class
Function တွေကို class ထဲမှာကြေညာလို့ရပါတယ်။
```python
#code here
```
class ထဲမှာ function ကိုဖန်တီးတဲ့အခါမှာ (self) ဆိုပီးထည့်ထားတာတွေ့ရပါမယ်။အဲ့လိုထည့်ထားမှသာ class ထဲမှာရှိတဲ့ variable ကိုလှမ်းခေါ်လို့ရပါလိမ့်မယ်။

### Constructor
class တစ်ခုစပြီးဆောက်တဲ့အခါမှာတန်ဖိုးတွေကိုထည့်လိုက်ချင်တယ်။ဒါမှမဟုတ်တန်ဖိုးတစ်ခုခုကိုကြိုထည့်ထားမယ်ဆိုရင် def _init_(self) ကိုအသုံးပြုနိုင်ပါတယ်။constructorလို့ခေါ်ပါတယ်။
```python
#code here
```
