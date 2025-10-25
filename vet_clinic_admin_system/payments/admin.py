from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "appointment",
        "get_pet_name",
        "get_vet_name",
        "type",
        "status",
        "value",
        "date",
        "active",
        "created_at",
    )
    list_display_links = ("id", "appointment")
    list_filter = ("type", "status", "active", "date", "created_at")
    search_fields = (
        "appointment__pet__name",
        "appointment__vet__username",
        "type",
        "status",
    )
    ordering = ("-date",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Payment Details", {
            "fields": (
                "appointment",
                "type",
                "status",
                "value",
                "date",
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