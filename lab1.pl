%Задание 6
%Медведь большой. Слон большой. Кот маленький
big(bear).
big(elephant).
small(cat).

%Медведь коричневый. Слон серый. Кот черный
color(bear, brown).
color(cat, black).
color(elephant, gray).

%Любой черный или коричневый предмет является темным
dark(X) :- color(X, brown) ; color(X, black).

%Кто одновременно большой и темный?
?-dark(Y), big(Y).

%Есть ли коричневые маленькие слоны?
?-color(elephant, brown), small(elephant).

%Есть ли большие и темные медведи?
?-big(bear), dark(bear).

%Есть ли черный кот?
?-color(cat, black).

