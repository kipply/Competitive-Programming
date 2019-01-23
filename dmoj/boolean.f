program banana
    integer :: n, l, cute
    character(len=1000) :: line
    read(*,'(A)') line
    l = len_trim(line)
    n = MODULO(l,4) 
    cute = MODULO(l/4, 2)
    
    IF (n == 0) THEN
        IF (cute == 0) THEN
            print*,"False"
        ELSE 
            print*, "True"
        ENDIF
    ELSE 
        IF (cute == 0) THEN
            print*,"True"
        ELSE 
            print*, "False"
        ENDIF

    ENDIF
    
end program banana
