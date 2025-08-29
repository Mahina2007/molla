from django.db.models import Count, F, Avg
from django.utils import timezone

from apps.pages.models import Section, Course, Student, Instructor, Enrollment, ExamResult


# ========= HOMEWORK (QUERY) LAR =========

# BASIC
def run():
    def homework1_get_courses_without_enrollments():
        """Hech bir sectionida yozilish boвЂlmagan fanlarni qaytaradi"""
        courses = Course.objects.exclude(sections__enrollments__isnull = False)
        print(courses)

    def homework2_get_students_not_enrolled_in_term(term_id):
        """Berilgan termda umuman yozilmagan talabalarni qaytaradi"""
        students = Student.objects.exclude(enrollments__section__term_id=term_id)
        print(students)

    def homework3_get_instructors_with_full_sections(term_id):
        """Berilgan termda to'liq to'lgan (capacity ga teng) sectionlari bor o'qituvchilarni qaytaradi"""
        full_sections = Section.objects.annotate(
        enrolled_count=Count('enrollments')
        ).filter(
        term_id=term_id,
        enrolled_count=F('capacity')
        )
        instructors = Instructor.objects.filter(sections__in=full_sections).distinct()
        print(instructors)

    def homework4_get_overbooked_sections(term_id):
        """Capacity dan ortiq yozilgan sectionlarni (xato holat) topadi"""
        overbooked_sections = Section.objects.annotate(
            enrolled_count=Count('enrollments')
        ).filter(
            term_id=term_id,
            enrolled_count__gt =F('capacity')
        )
        print(overbooked_sections)

    def homework5_get_top_students_in_course(course_code, term_id, limit=5):
        """Kurs bo'yicha eng yuqori o'rtacha imtihon balliga ega talabalarni qaytaradi"""
        top_students = Student.objects.filter(
            exam_results__exam_course=course_code,
            exam_results__exam__term_id=term_id
        ).annotate(
            avg_score=Avg('exam_results__score')
        ).order_by('-avg_score')[:limit]
        print(top_students)


    def homework6_get_all_active_students():
        """Faol (is_active=True) talabalarni qaytaradi"""
        active_students = Student.objects.filter(is_active=True)
        print(active_students)

    def homework7_get_courses_in_department(department_id):
        """Berilgan kafedradagi fanlarni qaytaradi"""
        courses = Course.objects.filter(department_id=department_id)
        print(courses)

    def homework8_get_instructors_in_department(department_name):
        """Berilgan kafedradagi o'qituvchilarni qaytaradi"""
        instructors = Instructor.objects.filter(department__name=department_name)
        print(instructors)

    def homework9_get_students_by_year(year):
        """Berilgan kurs (year_of_study) dagi talabalarni qaytaradi"""
        students = Student.objects.filter(year_of_study = year)
        print(students)

    def homework10_get_sections_for_course(course_code):
        """Berilgan kursga tegishli barcha sectionlarni qaytaradi"""
        sections = Course.objects.filter(course__code= course_code)
        print(sections)

    def homework11_get_students_born_this_year():
        """Hozirgi yilda tug'ilgan talabalarni qaytaradi"""
        current_year = timezone.now().year
        students = Student.objects.filter(birth_date__year=current_year)
        print(students)

    def homework12_get_courses_taught_by_instructor(instructor_id):
        """Berilgan instructor tomonidan o'tiladigan fanlarni qaytaradi"""
        courses = Course.objects.filter(sections__instructor_id= instructor_id).distinct()
        print(courses)

    def homework13_get_courses_without_prerequisites():
        """Hech qanday prerequisite talab qilmaydigan fanlarni qaytaradi"""
        courses = Course.objects.filter(prereqs_for__isnull=True)
        print(courses)

    def homework14_get_enrollments_of_student(student_id):
        """Berilgan talabaning barcha yozilishlarini qaytaradi"""
        enrollments = Enrollment.objects.filter(student_id = student_id)
        print(enrollments)

    def homework15_get_exam_results_of_student(student_id):
        """Berilgan talabaning barcha imtihon natijalarini qaytaradi"""
        results = ExamResult.objects.filter(student_id=student_id)
        print(results)

if __name__ == '__main__':
    run()