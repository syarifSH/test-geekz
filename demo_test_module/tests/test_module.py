# -*- coding: utf-8 -*-

from odoo.tests import common


class TestModule(common.TransactionCase):

    def test_create_data(self):
        # Create a new project with the test
        test_material_supplier = self.env['material.supplier'].create({
            'name': 'CreateSupplier'
        })

        # Add a test task to the project
        test_material_material = self.env['material.material'].create({
            'name': 'ExampleMaterial',
            'supplier_id': test_material_supplier.id
        })

        # Check if the project name and the task name match
        self.assertEqual(test_material_supplier.name, 'CreateSupplier')
        self.assertEqual(test_material_material.name, 'ExampleMaterial')
        # Check if the project assigned to the task is in fact the correct id
        self.assertEqual(test_material_material.supplier_id.id, test_material_material.id)
        # Do a little print to show it visually for this demo - in production you don't really need this.
        print('Your test was succesfull!')

        # # Create a new project with the test
        # test_project = self.env['project.project'].create({
        #     'name': 'TestProject'
        # })
        #
        # # Add a test task to the project
        # test_project_task = self.env['project.task'].create({
        #     'name': 'ExampleTask',
        #     'project_id': test_project.id
        # })
        #
        # # Check if the project name and the task name match
        # self.assertEqual(test_project.name, 'TestProject')
        # self.assertEqual(test_project_task.name, 'ExampleTask')
        # # Check if the project assigned to the task is in fact the correct id
        # self.assertEqual(test_project_task.project_id.id, test_project.id)
        # # Do a little print to show it visually for this demo - in production you don't really need this.
        # print('Your test was succesfull!')