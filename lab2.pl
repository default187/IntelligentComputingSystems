%Вариант 13
replace(_, _, [], []).
replace(Element, 0, [_|Tail], [Element|Tail]).
replace(Element, Index, [Head|Tail], [Head|NewTail]) :-
    Index > 0,
    NextIndex is Index - 1,
    replace(Element, NextIndex, Tail, NewTail).
