from django.contrib import admin
from cfp.models import CallForPaper, PaperApplication, Applicant
from django.core import urlresolvers


def mark_as_excluded(modeladmin, request, queryset):
    queryset.update(exclude=True)


class ApplicantAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', )
    list_display = ('user', 'full_name', 'about', 'biography', 'speaker_experience', 'github', 'twitter')
    fields = ('user', 'about', 'biography', 'speaker_experience', 'image')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields


class PaperApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_to_applicant', 'about', 'abstract', 'skill_level',
            'duration', 'exclude', 'accomodation_required', 'extra_info', 'votes_count')
    fields = ('cfp', 'applicant', 'title', 'about', 'abstract', 'skill_level',
            'duration', 'extra_info', 'accomodation_required')
    actions = [mark_as_excluded]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('cfp', 'applicant')
        return self.readonly_fields

    def link_to_applicant(self, obj):
        link = urlresolvers.reverse("admin:cfp_applicant_change", args=[obj.applicant.id])
        return u'<a href="%s">%s</a>' % (link, obj.applicant)
    link_to_applicant.allow_tags = True

admin.site.register(CallForPaper)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(PaperApplication, PaperApplicationAdmin)
