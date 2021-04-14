# # def message(str):
# #     def addWelcome():
# #         return "Welcome To"
# #     return addWelcome() + str
# # def site(site_name):
# #     return site_name
# # print(message(site("Python class"))
def message(fun):
      def addWelcome(site_name):
          return "Welcome To" + fun(site_name)
      return addWelcome
@message
def site(site_name):
      return site_name
print(site("Python class"))
