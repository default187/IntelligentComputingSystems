%������� �������. ���� �������. ��� ���������
big(bear).
big(elephant).
small(cat).

%������� ����������. ���� �����. ��� ������
color(bear, brown).
color(cat, black).
color(elephant, gray).

%����� ������ ��� ���������� ������� �������� ������
dark(X) :- color(X, brown) ; color(X, black).

%��� ������������ ������� � ������?
?-dark(Y), big(Y).

%���� �� ���������� ��������� �����?
?-color(elephant, brown), small(elephant).

%���� �� ������� � ������ �������?
?-big(bear), dark(bear).

%���� �� ������ ���?
?-color(cat, black).

