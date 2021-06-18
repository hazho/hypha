# Generated by Django 2.2.24 on 2021-06-18 04:54

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0036_add_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorformsettings',
            name='account_holder_name_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='This name must be same as the person or organisation that signed the contract. This person is authorised to sign contracts on behalf of the person or organisation named above.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='account_number_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Depending on your country, this might be called the account number, IBAN, or BBAN number.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='account_routing_number_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Depending on your country, this might be called the ACH, SWIFT, BIC or ABA number.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='branch_address_help_text',
            field=models.TextField(blank=True, default='The address of the bank branch where you have the bank account located(not the bank account holder address)', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='due_diligence_documents_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Upload Due Diligence Documents. E.g. w8/w9 forms.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='ib_account_currency_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='This is the currency of this bank account', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='ib_account_number_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Depending on your country, this might be called the account number, IBAN, or BBAN number', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='ib_account_routing_number_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Depending on your country, this might be called ACH, SWIFT, BIC or ABA number', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='ib_branch_address_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='Bank branch address(not the bank account holder address)', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='need_extra_info_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='nid_number_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='nid_type_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='This could be a passport, a National Identity number, or other national identity document.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='other_info_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='If you need to include other information not listed above, provide it here.', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='required_to_pay_taxes_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='', verbose_name='help text'),
        ),
        migrations.AlterField(
            model_name='vendorformsettings',
            name='type_help_text',
            field=wagtail.core.fields.RichTextField(blank=True, default='The name of the bank account must be the same as on the contract.', verbose_name='help text'),
        ),
    ]
