# #!/usr/bin/python3
# # test_rectangle.py
# # AbdulTechX
# """Defines unittests for models/rectangle.py.

# Unittest classes:
#     TestRectangle_instantiation - line 25
#     TestRectangle_width - line 114
#     TestRectangle_height - line 190
#     TestRectangle_x - line 262
#     TestRectangle_y - line 334
# """
# from models.base import Base
# from models.rectangle import Rectangle


#     def test_rectangle_is_base(self):
#         self.assertIsInstance(Rectangle(10, 2), Base)

#     def test_no_args(self):
#         with self.assertRaises(TypeError):
#             Rectangle()

#     def test_one_arg(self):
#         with self.assertRaises(TypeError):
#             Rectangle(1)

#     def test_two_args(self):
#         r1 = Rectangle(10, 2)
#         r2 = Rectangle(2, 10)
#         self.assertEqual(r1.id, r2.id - 1)

#     def test_three_args(self):
#         r1 = Rectangle(2, 2, 4)
#         r2 = Rectangle(4, 4, 2)
#         self.assertEqual(r1.id, r2.id - 1)
