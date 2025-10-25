from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "appointment",
        "get_pet_name",
        "get_vet_name",
        "diagnosis",
        "follow_up_date",
        "active",
        "created_at",
    )
    list_display_links = ("id", "appointment")
    list_filter = ("active", "created_at", "follow_up_date")
    search_fields = (
        "appointment__pet__name",
        "appointment__vet__username",
        "diagnosis",
        "treatment",
        "symptoms",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Medical Record Details", {
            "fields": (
                "appointment",
                "symptoms",
                "diagnosis",
                "treatment",
                "prescription",
                "follow_up_date",
                "active",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def get_pet_name(self, obj):
        return obj.appointment.pet.name
    get_pet_name.short_description = "Pet"

    def get_vet_name(self, obj):
        return obj.appointment.vet.username
    get_vet_name.short_description = "Vet"