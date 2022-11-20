class Profile:
    def __init__(self,username:str,password:str):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) <= 15 and len(value) > 5:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_len_valid(value) and self.contains_digit(value) and self.contains_upper_char(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_len_valid(self,value):
        return len(value) >= 8

    def contains_upper_char(self,value):
        upper_char = [char for char in value if char.isupper()]
        return True if upper_char else False

    def contains_digit(self,value):
        digits = [char for char in value if char.isdigit()]
        return True if digits else False

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*'*len(self.password)}"

# # profile_with_invalid_password = Profile('My_username', 'My-password')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)