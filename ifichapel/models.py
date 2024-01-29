from django.db import models

class Baptism(models.Model):
    full_mother_name = models.CharField(max_length=150, blank=False)
    full_father_name = models.CharField(max_length=150, blank=False)
    full_child_name = models.CharField(max_length=150,  blank=False)
    gen = ('M', 'Male'), ('F', 'Female')
    gender = models.CharField(max_length=150, blank=False, choices=gen)
    nationality_of_child = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=200, blank=False)
    contact_number = models.IntegerField(blank=False)
    xerox_copy_birth_certificate = models.FileField(upload_to='bapfiles/', blank=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_child_name

class Funerals(models.Model):
        full_mother_name = models.CharField(max_length=150, blank=False)
        full_father_name = models.CharField(max_length=150, blank=False)
        full_deceased_name = models.CharField(max_length=150, blank=False)
        gen = ('M', 'Male'), ('F', 'Female')
        gender = models.CharField(max_length=150, blank=False, choices=gen)
        nationality_of_deceased = models.CharField(max_length=150, blank=False)

        date_of_birth_deceased = models.CharField(max_length=150, blank=False)
        date_of_death_deceased = models.CharField(max_length=150, blank=False)

        address = models.CharField(max_length=200, blank=False)
        contact_number = models.IntegerField(blank=False)
        xerox_copy_death_certificate = models.FileField(upload_to='funeralfiles/', blank=False)
        date_created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.full_deceased_name

class Marriage(models.Model):
            full_groom_name = models.CharField(max_length=150, blank=False)
            full_groom_father_name = models.CharField(max_length=150, blank=False)
            full_groom_mother_name = models.CharField(max_length=150, blank=False)
            groom_birthday = models.CharField(max_length=150, blank=False)
            full_bride_name = models.CharField(max_length=150, blank=False)
            full_bride_father_name = models.CharField(max_length=150, blank=False)
            full_bride_mother_name = models.CharField(max_length=150, blank=False)
            bride_birthday = models.CharField(max_length=150, blank=False)

            groom_nationality = models.CharField(max_length=150, blank=False)
            bride_nationality = models.CharField(max_length=150, blank=False)
            contact_number = models.IntegerField(blank=False)
            xerox_copy_license_marriage = models.FileField(upload_to='marriagefiles/', blank=False)
            xerox_copy_baptismal_confirmation = models.FileField(upload_to='marriagefiles/', blank=False)
            date_created = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return self.full_groom_name

class Blessing(models.Model):
            full_name = models.CharField(max_length=150, blank=False)
            address = models.CharField(max_length=150, blank=False)

            watbless = ('H', 'House'), ('V', 'Vehicle'), ('I', 'Item')
            what_to_bless = models.CharField(max_length=150, blank=False, choices=watbless)
            contact_number = models.IntegerField(blank=False)
            xerox_copy_valid_ID = models.FileField(upload_to='blessingfiles/', blank=False)
            date_created = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return self.full_name

class Contact(models.Model):
                full_name = models.CharField(max_length=150, blank=False)
                contact_number = models.IntegerField(blank=False)
                concern_type = models.CharField(max_length=150, blank=False)
                message = models.CharField(max_length=200, blank=False)


                def __str__(self):
                    return self.full_name



class SchedStatus(models.Model):
    baptism = models.ManyToManyField(Baptism, related_name='client', blank=True)
    funeral = models.ManyToManyField(Funerals, related_name='client', blank=True)
    marriage = models.ManyToManyField(Marriage, related_name='client', blank=True)
    blessing = models.ManyToManyField(Blessing, related_name='client', blank=True)

    Stat = ('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')
    Status = models.CharField(max_length=100, choices=Stat)


class paying(models.Model):
    desired_date_of_schedule = models.CharField(max_length=150, blank=False)
    upload_receipt = models.FileField(upload_to='paymentreceipts/', blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    baptismz = models.ManyToManyField(Baptism, related_name='person', blank=True)
    funeralz = models.ManyToManyField(Funerals, related_name='person', blank=True)
    marriagez = models.ManyToManyField(Marriage, related_name='person', blank=True)
    blessingz = models.ManyToManyField(Blessing, related_name='person', blank=True)

    def __str__(self):
        return self.desired_date_of_schedule




