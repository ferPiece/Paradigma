%Programacion_Logica

%hechos
reserva(docente, laboratorio).
tiene(laboratorio, ficha).
nombre_proyecto('Reserva de Laboratorio').
posee(laboratorio,cantidad_maquinas).

%lista_de_laboratorios_existentes
laboratorios([algoritmos, hpc, redes_de_computadoras, modelado_y_simulacion, sistemas_operativos, base_de_datos, inteligencia_artificial]).

%lista_de_docentes_existentes
docente([cynthia, ramona, fernando, adrian, david, karina, hyroshi]).


%reglas
%si_es_docente_de_la_facultad
es_docente(X) :- docente(Lista), es_miembro(X, Lista). 

%Compara_si_un_elemento_se_encuetra_dentro_de_la_lista
es_miembro(X,[X|_]).
es_miembro(X,[_|Resto]):-es_miembro(X, Resto).

