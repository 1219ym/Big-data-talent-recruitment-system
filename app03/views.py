
# Create your views here.
from django.shortcuts import render
from .forms import ResumeForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from app03.models import Resume
def cares(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'success.html')
    else:
        form = ResumeForm()
    return render(request, 'cares.html', {'form': form})
def generate_pdf(request):
    # 获取数据
    data = Resume.objects.all()

    # 创建PDF文档
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mydocument.pdf"'
    p = canvas.Canvas(response)

    # 添加数据到PDF文档
    for item in data:
        # 添加个人信息
        p.drawString(100, 750, 'Name: {}'.format(item.first_name))
        p.drawString(100, 730, 'Middle Name: {}'.format(item.middle_name))
        p.drawString(100, 710, 'Last Name: {}'.format(item.last_name))
        p.drawString(100, 690, 'DOB: {}'.format(item.birth_date))
        p.drawString(100, 670, 'Gender: {}'.format(item.gender))
        p.drawString(100, 650, 'Marital Status: {}'.format(item.marital_status))
        p.drawString(100, 630, 'City: {}'.format(item.city))
        p.drawString(100, 610, 'Province: {}'.format(item.province))
        p.drawString(100, 590, 'Country: {}'.format(item.country))
        p.drawString(100, 570, 'Phone: {}'.format(item.phone_number))
        p.drawString(100, 550, 'Email: {}'.format(item.email))
        p.drawString(100, 530, 'Website: {}'.format(item.website))
        p.drawString(100, 510, 'Address: {}'.format(item.address))

        # 添加教育背景信息
        p.drawString(100, 470, 'Education:{}'.format(item.education_info))
        p.drawString(100, 450, 'University: {}'.format(item.university))
        p.drawString(100, 430, 'Degree: {}'.format(item.degree))
        p.drawString(100, 410, 'Major: {}'.format(item.major_name))

        # 添加工作经验信息
        p.drawString(100, 350, 'Company: {}'.format(item.company_name))
        p.drawString(100, 330, 'Position: {}'.format(item.position))
        p.drawString(100, 310, 'Region: {}'.format(item.location))
        p.drawString(100, 290, 'Start Date: {}'.format(item.start_date))
        p.drawString(100, 270, 'End Date: {}'.format(item.end_date))
        p.drawString(100, 250, 'Skills: {}'.format(item.skill_name))
        p.drawString(100, 230, 'Proficiency: {}'.format(item.proficiency))

        # 结束一页
        p.showPage()

    # 关闭PDF文档
    p.save()
    return response