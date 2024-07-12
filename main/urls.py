from . import views
from django.urls import path
urlpatterns = [
    path('passGrievance/<int:id>', views.passGrievance,name="passGrievance"),
    path('rejectGrievance/<int:id>', views.rejectGrievance,name="rejectGrievance"),
    path('solveGrievance/<int:id>', views.solveGrievance,name="solveGrievance"),


    path('', views.index,name="index"),
    path('manageLogin/', views.manageLogin,name="manageLogin"),
    path('manageLogout/',views.manageLogout,name='manageLogout'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('function_forgot/',views.function_forgot,name='function_forgot'),
    path('verify/',views.verify,name='verify'),
    path('reset_password/',views.reset_password,name='reset_password'),

    path('Function_Change/',views.Function_Change,name='Function_Change'),
    path('Change_Password/',views.Change_Password,name='Change_Password'),

    path('complain_form/', views.complain_form,name="complain_form"),
    path('for_solve_grievance/', views.for_solve_grievance,name="for_solve_grievance"),
    path('addComplain/', views.addComplain,name="addComplain"),
    path('show_your_grievance/', views.show_your_grievance,name="show_your_grievance"),
    path('feedback/<str:id>', views.feedback,name="feedback"),

    
    path('updateProfile/<str:name>', views.updateProfile,name="updateProfile"),
    path('account/', views.account,name="account"),
    
    path('manageCollage/', views.manageCollage,name="manageCollage"),
    path('addCollage/',views.addCollage,name='addCollage'),
    path('deleteCollage/<int:id>', views.deleteCollage, name='deleteCollage'),
    path('updateCollage/<int:id>', views.updateCollage, name='updateCollage'),

    path('manageDepartment/', views.manageDepartment,name="manageDepartment"),
    path('addDepartment/',views.addDepartment,name='addDepartment'),
    path('deleteDepartment/<int:id>', views.deleteDepartment, name='deleteDepartment'),
    path('updateDepartment/<int:id>', views.updateDepartment, name='updateDepartment'),

    path('manageDesignation/',views.manageDesignation,name='manageDesignation'),
    path('addDesignation/',views.addDesignation,name='addDesignation'),
    path('deleteDesignation/<int:id>', views.deleteDesignation, name='deleteDesignation'),
    path('updateDesignation/<int:id>', views.updateDesignation, name='updateDesignation'),

    path('manageGrievanceType/',views.manageGrievanceType,name='manageGrievanceType'),
    path('addCategory/',views.addCategory,name='addCategory'),
    path('deleteCategory/<int:id>', views.deleteCategory, name='deleteCategory'),
    path('updateCategory/<int:id>', views.updateCategory, name='updateCategory'),

    path('manageUsers/',views.manageUsers,name='manageUsers'),
    path('addUser/',views.addUser,name='addUser'),
    path('updateUser/<int:id>',views.updateUser,name='updateUser'),
    path('deleteUser/<int:id>',views.deleteUser,name='deleteUser'),

    path('downloadCsvMenu/',views.downloadCsvMenu,name='downloadCsvMenu'),
    path('uploadCsvMenu/',views.UploadCsvMenu,name='uploadCsvMenu'),

    path('reg_report/',views.reg_report,name='reg_report'),
    path('render_pdf_view/',views.render_pdf_view,name='render_pdf_view'),

    ]