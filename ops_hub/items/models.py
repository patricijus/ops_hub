from django.db import models

class Item(models.Model):

    # Add choices at the top of the class
    PRODUCTION_LINE_CHOICES = [
        ('Production Line 1', 'Production Line 1'),
        ('Production Line 2', 'Production Line 2'),
        ('Production Line 3', 'Production Line 3'),
        ('Production Line 4', 'Production Line 4'),
        ('Production Line 5', 'Production Line 5'),
        ('Production Line 6', 'Production Line 6'),
    ]
    PRODUCT_CATEGORY_CHOICES = [
        ('Burgers', 'Burgers'),
        ('Sausages', 'Sausages'),
        ('Meatballs', 'Meatballs'),
    ]


    name = models.CharField(max_length=255)
    supplier_code = models.CharField(max_length=50)
    weight_per_tray = models.DecimalField(max_digits=10, decimal_places=2)
    trays_per_carton = models.IntegerField()
    carton_type = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    upc_code = models.CharField(max_length=50)
    tray_type = models.CharField(max_length=100)
    shelf_life = models.IntegerField(help_text="Shelf life in days")
    mlor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Minimum life on receival")
    primary_pack_weight = models.CharField(max_length=100)
    item_class = models.CharField(max_length=100, choices=PRODUCT_CATEGORY_CHOICES)
    secondary_label = models.CharField(max_length=255)
    cartons_per_pallet = models.IntegerField()
    item_demand = models.IntegerField(help_text="This is item demand number from Netsuite")
    run_rate = models.DecimalField(max_digits=6, decimal_places=2, help_text="This number x 60 x 24 gives number of trays per hour")
    production_line = models.CharField(max_length=50, choices=PRODUCTION_LINE_CHOICES)
    alternative_production_line = models.CharField(max_length=50, choices=PRODUCTION_LINE_CHOICES, blank=True, null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
