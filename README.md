### 环境  
openGauss 5.1.0  
Django 3.0.0  

```bash
pip install Django==3.0.0
```
将`connect_db`中`setting.py`的`DATABASE`修改  
```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_project', #数据库名
        'USER': 'admin', #用户名
        'PASSWORD': 'Gauss@123', #密码
        'HOST': '192.168.56.109',#虚拟机ip
        'PORT': 26000 #openGauss数据口的端口
    }
}
```
执行以下命令运行服务器  
```
# 生成迁移文件
python manage.py makemigrations
# 执行sql语句生成数据表
python manage.py migrate
# 运行服务器
python manage.py runserver
```



### 功能演示  
#### 患者  
* ##### 预约挂号:  
* - 可以通过医生姓名或者科室来筛选医生(支持模糊搜索), 点击对应医生的预约按钮进入预约界面  
![](img/patient/patient_register.jpg)  
* - 选择日期和时段后提交预约  
![](img/patient/patient_appoint.jpg)  
* ##### 医生介绍:  
* - 按科室展示所有医生, 点击医生的名字可以进入医生详情界面  
![](img/patient/patient_personnel.jpg)  
* - 医生详情界面可以看到医生的职称, 科室, 科室房间号, 以及简介信息  
![](img/patient/patient_profile.jpg)  
* ##### 挂号记录:
* - 可以看到已经预约的挂号记录, 当医生未开始接诊时(状态为已挂号), 可以点击取消预约来取消.  
![](img/patient/patient_registration.jpg)  
* - 当医生填写好病例, 并结束就诊后, 可以点击查看详情来查看诊断结果  
![](img/patient/patient_medicalrecord.jpg)  
* 个人中心:  
* - 可以看到患者的个人信息, 可进行注销账号操作  
![](img/patient/patient_personal.jpg)  


#### 医生  
* ##### 患者预约记录:  
* - 按照预约时间, 预约时段顺序对患者预约记录排序  
![](img/doctor/doctor_registration.jpg)  
* - 点击接诊后可以填写病例, 结束就诊  
![](img/doctor/doctor_medicalrecord.jpg)  
* ##### 药房:  
* - 可以根据药物名(支持模糊搜索)或药物类型来筛选药物:  
![](img/doctor/doctor_medicine.jpg)  
* ##### 个人中心:  
* - 可以看到医生的个人信息, 可进行账号注销操作:  
![](img/doctor/doctor_personal.jpg)  


