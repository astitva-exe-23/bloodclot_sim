; =============================================
; FINAL FIXED BLOOD CLOT RISK ASSESSMENT SYSTEM
; ATmega328P - 4-Level Risk Output (0-3)
; =============================================

.NOLIST
.INCLUDE "m328Pdef.inc"
.LIST

; --- Scaled Medical Thresholds (÷10) ---
.EQU PLATELET_LOW = 15   ; Originally 150
.EQU FIBRINOGEN_LOW = 15 ; Originally 150
.EQU CLOTTING_HIGH = 8    ; Originally 8
.EQU D_DIMER_HIGH = 50    ; Originally 500

; --- Register Usage ---
.DEF platelet = r18
.DEF fibrinogen = r19
.DEF clotting = r20
.DEF d_dimer = r21
.DEF risk = r22        ; Output: 0=Normal, 1=Low, 2=Medium, 3=High
.DEF temp = r23        ; Temporary counter

; --- Program Start ---
.CSEG
.ORG 0x0000
    rjmp main

main:
    ; Test Case 1: Normal (Risk 0)
    ldi platelet, 20
    ldi fibrinogen, 20
    ldi clotting, 5
    ldi d_dimer, 40
    rcall assess_risk   ; Should return risk=0

    ; Test Case 2: Low risk (Risk 1) - FIXED
    ldi platelet, 10    ; Only 1 abnormal parameter
    ldi fibrinogen, 20
    ldi clotting, 5
    ldi d_dimer, 40
    rcall assess_risk   ; Now correctly returns risk=1

    ; Test Case 3: Medium risk (Risk 2)
    ldi platelet, 10    ; 2 abnormal parameters
    ldi fibrinogen, 10
    ldi clotting, 5
    ldi d_dimer, 40
    rcall assess_risk   ; Returns risk=2

    ; Test Case 4: High risk (Risk 3)
    ldi platelet, 10    ; 3+ abnormal parameters
    ldi fibrinogen, 10
    ldi clotting, 10
    ldi d_dimer, 60
    rcall assess_risk   ; Returns risk=3

    rjmp main

; --- FINAL CORRECTED Risk Assessment ---
assess_risk:
    clr temp
    
    ; Check each parameter (max +1 per parameter)
    cpi platelet, PLATELET_LOW
    brsh plt_ok
    inc temp
plt_ok:

    cpi fibrinogen, FIBRINOGEN_LOW
    brsh fib_ok
    inc temp
fib_ok:

    cpi clotting, CLOTTING_HIGH
    brlo clot_ok
    inc temp
clot_ok:

    cpi d_dimer, D_DIMER_HIGH
    brlo dimer_ok
    inc temp
dimer_ok:

    ; FINAL RISK MAPPING (Simple and accurate)
    cpi temp, 1
    breq low_risk
    cpi temp, 2
    breq medium_risk
    cpi temp, 3
    brsh high_risk
    clr risk       ; temp=0 ? Normal
    ret

low_risk:
    ldi risk, 1    ; Exactly 1 abnormal ? Low risk
    ret

medium_risk:
    ldi risk, 2    ; Exactly 2 abnormal ? Medium risk
    ret

high_risk:
    ldi risk, 3    ; 3+ abnormal ? High risk
    ret

.ESEG