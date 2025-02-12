@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_PT.DIG', 'ef_emb_PT_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 18)


@State
def EMB_PT_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_PT.DIG', 'ef_emb_PT_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 18)


@State
def EMB_PT_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_PT.DIG', 'ef_emb_PT_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 8)
    ColorTransition(4294912040, 10)
    sprite('null', 8)
    ColorTransition(4294948020, 10)
    sprite('null', 8)
    ColorTransition(4294901760, 10)
    sprite('null', 18)


@State
def DebugObject():
    sprite('null', 2)
    loopRest()
    sprite('null', 30)
    CreateObject('Shabon', -1)


@State
def ShabonDist():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        ParticleTransparency(1)
        PlayerTransparency(12000)
        RenderLayer(1)

        def upon_33():
            sendToLabel(10)
    sprite('vr_shabon_dist', 32767)
    label(10)
    sprite('vr_shabon_dist', 8)
    SetScaleSpeed(20)
    ConstantAlphaModifier(-30)


@State
def Shabon1():
    sprite('vr_shabon00', 4)
    RenderLayer(1)
    sprite('vr_shabon01', 4)


@State
def Shabon2():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        EnemyHitstopAddition(0, 60, 60)
        Damage(800)
        AttackP1(80)
        AttackP2(95)
        SameMoveProration(10)
        GroundedHitstunAnimation(5)
        Hitstop(5)
        DamageEffect(7, 'runjump_water_l')
        AttackDirection(3)
        DistanceCheck(180000, -180000, 180000, -360000)
        OnlyHitPlayer(1)
        PassByArmor(1)
        IgnoreBurst(1)
        StarterRating(2)
        RenderLayer(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 10)
        Unknown23091(1)
        WallCollisionDetection(1)
        LandingHeight(135000)
        SetXCollisionFromOrigin(270)
        Unknown23180(1)
        SLOT_7 = 1

        def upon_STATE_END():
            SLOT_7 = 0

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_LANDING():
            YAccel(-50)

        def upon_OPPONENT_HIT_OR_BLOCK():
            NoDamageAction(1)

        def upon_14():
            AttackOff()
            Unknown23090(23)

        def upon_OPPONENT_HIT():
            sendToLabel(11)
            HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
        SetScaleX(1620)
        SetScaleY(1380)

        def upon_EVERY_FRAME():
            SLOT_52 = SLOT_52 + 1
            if not SLOT_52 % 30:
                if SLOT_51:
                    SLOT_51 = 0
                else:
                    SLOT_51 = 1
            if SLOT_51:
                AddScaleX(8)
                AddScaleY(-8)
            else:
                AddScaleX(-8)
                AddScaleY(8)
        CreateObject('ShabonDist', -1)
        RegisterObject(4, 1)
        CreateParticle('ptef_shaboncreate', -1)
    sprite('vr_shabon', 1)
    label(0)
    sprite('vr_shabon', 120)
    physicsXImpulse(3000)
    physicsYImpulse(4000)

    def upon_CORNERED():
        XImpulseAcceleration(-50)
    sprite('vr_shabon', 60)
    physicsYImpulse(0)
    setGravity(100)
    sprite('vr_shabon', 60)
    YSpeed(1000)
    setGravity(-200)
    sprite('vr_shabon', 60)
    YSpeed(-1000)
    setGravity(200)
    sprite('vr_shabon', 60)
    YSpeed(1000)
    setGravity(-200)
    sprite('vr_shabon', 60)
    YSpeed(-1000)
    setGravity(200)
    sprite('vr_shabon', 60)
    YSpeed(1000)
    setGravity(-200)
    sprite('vr_shabon', 60)
    YSpeed(-1000)
    setGravity(200)
    sprite('vr_shabon', 1)
    Unknown23090(23)
    loopRest()
    ExitState()
    label(1)
    sprite('vr_shabon', 12)
    physicsXImpulse(4000)
    XSpeed(4000)
    physicsYImpulse(-500)

    def upon_CORNERED():
        XImpulseAcceleration(-50)
    sprite('vr_shabon', 40)
    sprite('vr_shabon', 150)
    setGravity(-200)
    sprite('vr_shabon', 1)
    Unknown23090(23)
    loopRest()
    ExitState()
    label(2)
    sprite('vr_shabon', 500)
    physicsXImpulse(3000)
    physicsYImpulse(8000)
    setGravity(100)

    def upon_5():
        physicsYImpulse(9000)
    sprite('vr_shabon', 1)
    Unknown23090(23)
    loopRest()
    ExitState()
    label(11)
    sprite('vr_shabon', 1)
    AttackOff()
    WallCollisionDetection(0)
    PrivateSE('ptse_27')
    EffectPosition(22, 103)
    E0EAEffectPosition(22)
    IgnoreScreenfreeze(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Size(1200)
    SetScaleSpeed(125)
    ConstantAlphaModifier(40)

    def RunOnObject_4():
        PlayerTransparency(25000)
    sprite('vr_shabon', 12)
    sprite('vr_shabon', 43)
    AlphaValue(255)
    Size(2800)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    sprite('vr_shabon', 1)
    Unknown23090(23)
    loopRest()
    ExitState()
    label(10)
    sprite('vr_shabonkoware', 30)
    AttackOff()
    StartMultihit()
    setInvincible(1)
    SetScaleSpeed(20)
    ConstantAlphaModifier(-20)
    XImpulseAcceleration(40)
    YAccel(40)
    setGravity(0)
    EndAttack()
    CommonSE('207_runjump_water_0')
    CommonSE('207_runjump_water_0')
    TriggerUponForState('ShabonDist', 33)
    CreateParticle('ptef_shabonkoware', -1)
    ExitState()


@State
def test1_2():
    sprite('test1_pt204_07_lv2', 3000)
    AddY(300000)


@State
def test0():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        AddRotationPerFrame(7500)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
    sprite('test0_pt204_07_lv2', 300)


@State
def test1():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        AddRotationPerFrame(7500)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
    sprite('test2_pt204_07_lv2', 300)


@State
def test2():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        GroundedHitstunAnimation(9)
        Damage(550)
        AirUntechableTime(30)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
    sprite('test1_pt204_07_lv2', 300)


@Subroutine
def ItemThrowInit():
    AttackLevel_(5)
    Damage(850)
    AirPushbackX(30000)
    GroundedHitstunAnimation(9)
    AirUntechableTime(30)
    AttackP1(80)
    StarterRating(2)
    setGravity(400)
    physicsXImpulse(26000)
    physicsYImpulse(18000)


@State
def Hummer():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1200)
        HitAirUnblockable(3)
        DamageEffect(6, 'ptef_hit_pikohan_throw')
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_hummer', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_hummer', 30)
    StartMultihit()


@State
def __16t_Hummer():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1800)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        HitAirUnblockable(3)
        DamageEffect(6, 'ptef_hit_other_throw')
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_16thummer', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_16thummer', 30)
    StartMultihit()


@State
def Cat_Hummer():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(950)
        HitAirUnblockable(3)
        DamageEffect(6, 'ptef_hit_cat_throw')
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Cat_hummer', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Cat_hummer', 30)
    StartMultihit()


@State
def Lion_Hummer():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1500)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        HitAirUnblockable(3)
        DamageEffect(6, 'ptef_hit_other_throw')
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Lion_hummer', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Lion_hummer', 30)
    StartMultihit()


@State
def Frying__ds__pan():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(850)
        DamageEffect(6, 'ptef_hit_fripan_throw')
        HitAirUnblockable(3)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Frying-pan', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Frying-pan', 30)
    StartMultihit()


@State
def Harisen():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1300)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        DamageEffect(6, 'ptef_hit_harisen_throw')
        HitAirUnblockable(3)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Harisen', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Harisen', 30)
    StartMultihit()


@State
def Bat():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(900)
        DamageEffect(6, 'ptef_hit_bat_throw')
        HitAirUnblockable(3)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Bat', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Bat', 30)
    StartMultihit()


@State
def Kanabou():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1400)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        DamageEffect(6, 'ptef_hit_other_throw')
        HitAirUnblockable(3)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Kanabou', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_Kanabou', 30)
    StartMultihit()


@State
def PaletteControlObj1():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 1, 0, 0, 0, 0, 0, 0)
        AddX(50000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj2():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 3, 0, 0, 0, 0, 0, 0)
        AddX(100000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj3():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 5, 0, 0, 0, 0, 0, 0)
        AddX(150000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj4():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 7, 0, 0, 0, 0, 0, 0)
        AddX(200000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj5():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 9, 0, 0, 0, 0, 0, 0)
        AddX(250000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj6():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 11, 0, 0, 0, 0, 0, 0)
        AddX(300000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj7():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 13, 0, 0, 0, 0, 0, 0)
        AddX(300000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@State
def PaletteControlObj8():

    def upon_IMMEDIATE():
        TurnParticleColorable1(1)

        def upon_48():
            CallPrivateFunction('PT_Light', 0, 15, 0, 0, 0, 0, 0, 0)
        AddX(300000)
        AbsoluteY(-200000)
    sprite('null', 32767)


@Subroutine
def SetHikariColorByObjReg0():
    PrivateFunction(9, 2, 59, 0, 1, 2, 55)
    PrivateFunction(9, 2, 59, 0, 2, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-60396)
    PrivateFunction(9, 2, 59, 0, 3, 2, 55)
    PrivateFunction(9, 2, 59, 0, 4, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-15461121)
    PrivateFunction(9, 2, 59, 0, 5, 2, 55)
    PrivateFunction(9, 2, 59, 0, 6, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-15401196)
    PrivateFunction(9, 2, 59, 0, 7, 2, 55)
    PrivateFunction(9, 2, 59, 0, 8, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-690166)
    PrivateFunction(9, 2, 59, 0, 9, 2, 55)
    PrivateFunction(9, 2, 59, 0, 10, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-658171)
    PrivateFunction(9, 2, 59, 0, 11, 2, 55)
    PrivateFunction(9, 2, 59, 0, 12, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-16386571)
    PrivateFunction(9, 2, 59, 0, 13, 2, 55)
    PrivateFunction(9, 2, 59, 0, 14, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-64001)
    PrivateFunction(9, 2, 59, 0, 15, 2, 55)
    PrivateFunction(9, 2, 59, 0, 16, 2, 56)
    if not SLOT_55 or not SLOT_56:
        StopCharacterFlash1(-69999)


@State
def SphereLight():

    def upon_IMMEDIATE():

        def upon_16():
            Unknown23179(1)
            SLOT_59 = SLOT_4
            callSubroutine('SetHikariColorByObjReg0')

        def upon_53():
            EndObject()
        IgnoreScreenfreeze(1)
        SLOT_51 = 1

        def upon_48():
            MoveToCollision(3, 13, 0)

        def upon_45():
            SLOT_52 = SLOT_52 + 1
            if SLOT_51:
                if SLOT_28:
                    MoveToCollision(3, 13, 0)
                    if not SLOT_52 % 8:
                        CreateParticle('ptef_driveptc', -1)
                if not SLOT_28:
                    sendToLabel(0)
                    SLOT_51 = 0
                    TriggerUponForState('SphereLight_Model', 33)
                if not SLOT_4:
                    sendToLabel(0)
                    SLOT_51 = 0
                    TriggerUponForState('SphereLight_Model', 33)
            elif SLOT_28:
                if SLOT_4:
                    sendToLabel(1)
                    SLOT_51 = 1
        CreateObject('SphereLight_Model', -1)
    label(0)
    sprite('null', 32767)
    label(1)
    sprite('vr_sphere_light2', 20)
    Unknown23179(1)
    Unknown23180(1)
    BlendMode_Add()
    Size(0)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    SetScaleSpeed(100)
    AddRotationPerFrame(8000)
    SetZVal(500)
    if not SLOT_59 % 2:
        TriggerUponForState('SphereLight_Model', 32)
    loopRest()
    SetScaleSpeed(0)
    Size(2000)
    AddRotationPerFrame(800)
    AlphaValue(190)
    label(2)
    sprite('vr_sphere_light2', 4)
    AlphaValue(190)
    ConstantAlphaModifier(-17)
    sprite('vr_sphere_light2', 4)
    ConstantAlphaModifier(17)
    loopRest()
    gotoLabel(2)


@State
def SphereLight_Shutsugen():
    sprite('null', 30)
    CallPrivateEffect('ptef_drivepurg')
    CreateObject('yugami_ring', -1)
    IgnoreScreenfreeze(1)
    sprite('null', 30)
    ConstantAlphaModifier(-30)


@State
def SphereLight_Model():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_kurukuru.DIG', 'ptef_kurukuru_motion_000.mmot')
        FaceSpawnLocation()
        SetZVal(500)
        IgnoreScreenfreeze(1)

        def upon_53():
            EndObject()

        def upon_16():
            PrivateFunction3(2, 0, 0, 80, 1)
            Unknown23179(1)
            SLOT_59 = SLOT_4
            callSubroutine('SetHikariColorByObjReg0')
        Size(350)
        SetScaleZ(1000)
        AlphaValue(0)

        def upon_32():
            ConstantAlphaModifier(30)
            Unknown23179(1)
            SLOT_59 = SLOT_4
            callSubroutine('SetHikariColorByObjReg0')

        def upon_33():
            ConstantAlphaModifier(-30)
    sprite('null', 32767)


@State
def StaggerSoul():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        AbsoluteY(270000)
        AddX(50000)
        AlphaValue(220)
    sprite('vrptef070_00', 8)
    physicsYImpulse(2000)
    sprite('vrptef070_00', 14)
    ConstantAlphaModifier(-10)
    sprite('vrptef070_00', 10)
    ConstantAlphaModifier(-20)


@State
def ptef_hit_low():
    sprite('null', 1)
    CreateParticle('ptef_hit_low', -1)
    PrivateSE('ptse_15')


@State
def ptef_hit_middle():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_16')


@State
def ptef_hit_high():
    sprite('null', 1)
    CreateParticle('ptef_hit_high', -1)
    PrivateSE('ptse_17')


@State
def ptef_hit_fripan():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_18')
    CommonSE('102_hit_counter_grap_1')


@State
def ptef_hit_harisen():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_19')


@State
def ptef_hit_bat():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_20')
    CommonSE('102_hit_counter_grap_1')


@State
def ptef_hit_pikohan_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_02')


@State
def ptef_hit_fripan_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_18')
    CommonSE('102_hit_counter_grap_1')


@State
def ptef_hit_harisen_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_19')
    CommonSE('100_hit_grap_2')


@State
def ptef_hit_bat_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_20')
    CommonSE('102_hit_counter_grap_1')


@State
def ptef_hit_cat_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    PrivateSE('ptse_24')


@State
def ptef_hit_other_throw():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    CommonSE('100_hit_grap_2')


@State
def ptef_hit_kanabou():
    sprite('null', 1)
    CreateParticle('ptef_hit_middle', -1)
    CommonSE('025_cleanhit_grap')


@State
def ptef_hit_throw():
    sprite('null', 1)
    CreateParticle('ptef_throw', -1)
    PrivateSE('ptse_18')
    CommonSE('102_hit_counter_grap_1')


@State
def Atk6CZanzo():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        AbsoluteY(420000)
        AddX(-20000)
    sprite('vrptef212_00', 3)
    sprite('vrptef212_01', 3)
    ConstantAlphaModifier(-10)
    sprite('vrptef212_02', 3)
    sprite('vrptef212_02', 3)
    ConstantAlphaModifier(-45)
    AddX(-20000)
    AddY(-5000)


@State
def ThrowBind():

    def upon_IMMEDIATE():
        E0EAEffectPosition(22)
        Eff3DEffect('ptef_bind.DIG', 'ptef_bind_motion_000.mmot')
        FaceSpawnLocation()
        BlendMode_Add()
        Size(1000)
        AddY(-40000)
    sprite('null', 38)
    sprite('null', 20)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(30)


@State
def ThrowMcircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_kousokucircle.DIG', 'ptef_kousokucircle_motion_000.m'
            )
        FaceSpawnLocation()
        BlendMode_Add()
        Size(1100)
        AddY(-40000)
        uponSendToLabel(32, 12)
    sprite('null', 8)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('null', 30)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-35)
    SetScaleSpeed(75)


@State
def Throwef():

    def upon_IMMEDIATE():
        LinkParticle('ptef_throwef')
        BlendMode_Add()
        Size(900)
        AddY(-20000)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(40)
    sprite('null', 35)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-20)


@State
def ThrowKousoku():
    sprite('null', 4)
    CreateObject('ThrowMcircle', 1)
    CreateObject('Throwef', 1)
    sprite('null', 1)
    CreateObject('ThrowBind', 1)


@State
def MagicIron():

    def upon_IMMEDIATE():
        AlphaValue(255)
        BlendMode_Normal()
        OnlyHitPlayer(1)
        IgnorePauses(3)

        def upon_32():
            AddX(-600000)
            AddY(100000)
            sendToLabel(0)

        def upon_33():
            AddX(600000)
            AddY(100000)
            sendToLabel(1)

        def upon_34():
            AddX(-15000)
            AddY(250000)
            sendToLabel(2)
    sprite('null', 1)
    label(0)
    sprite('vrptef311_00', 32767)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        sendToLabel(3)
    CommonSE('016_explode_1')
    physicsXImpulse(0)
    SetAcceleration(2000)
    physicsYImpulse(-10000)
    setGravity(-200)
    Visibility(0)
    uponSendToLabel(35, 3)
    loopRest()
    ExitState()
    label(1)
    sprite('vrptef311_00', 32767)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        sendToLabel(4)
    CommonSE('016_explode_1')
    physicsXImpulse(0)
    SetAcceleration(-1500)
    physicsYImpulse(-10000)
    setGravity(-200)
    uponSendToLabel(36, 4)
    loopRest()
    ExitState()
    label(2)
    sprite('vrptef311_00', 32767)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        sendToLabel(5)
    CommonSE('016_explode_1')
    physicsXImpulse(0)
    physicsYImpulse(-36000)
    uponSendToLabel(37, 5)
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef311_00', 1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(-10000)
    physicsYImpulse(31000)
    setGravity(3000)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('vrptef311_00', 20)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(4)
    sprite('vrptef311_00', 1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(10000)
    physicsYImpulse(31000)
    setGravity(3000)
    XImpulseAcceleration(90)
    YAccel(90)
    sprite('vrptef311_00', 20)
    ConstantAlphaModifier(-10)
    loopRest()
    ExitState()
    label(5)
    sprite('vrptef311_00', 20)
    LandingHeight(135000)

    def upon_LANDING():
        StartMultihit()
        SetAcceleration(0)
        physicsXImpulse(0)
        physicsYImpulse(31000)
        setGravity(3000)
        XImpulseAcceleration(90)
        YAccel(90)
        ConstantAlphaModifier(-10)
    sprite('vrptef311_00', 20)
    loopRest()
    ExitState()


@State
def Kemuri():

    def upon_IMMEDIATE():
        LinkParticle('ptef_311smoke')
        BlendMode_Normal()
        AddX(-600000)
        AddY(100000)
    sprite('null', 40)


@State
def Kemuri2():

    def upon_IMMEDIATE():
        LinkParticle('ptef_311smoke')
        BlendMode_Normal()
        AddX(600000)
        AddY(100000)
    sprite('null', 40)


@State
def Kemuri3():

    def upon_IMMEDIATE():
        LinkParticle('ptef_311smoke')
        BlendMode_Normal()
        AddY(200000)
    sprite('null', 40)


@State
def Kemuri4():

    def upon_IMMEDIATE():
        LinkParticle('ptef_311smoke')
        BlendMode_Normal()
        TeleportToObject(22)
        AddX(-15000)
        AddY(500000)
    sprite('null', 40)


@State
def pt203_mahojin():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_mahojin1.DIG', 'ptef_mahojin1_motion_000.mmot')
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(600)
        AddY(20000)
    sprite('null', 20)
    sprite('null', 30)
    E0EAEffectPosition(0)
    sprite('null', 13)
    ConstantAlphaModifier(-20)


@State
def pt203_airmahojin():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_mahojin1.DIG', 'ptef_mahojin1_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(600)
        AddY(20000)
    sprite('null', 20)
    sprite('null', 30)
    E0EAEffectPosition(0)
    sprite('null', 13)
    ConstantAlphaModifier(-30)


@State
def pt203_aura1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RenderLayer(5)
        AddY(8000)
        SetScaleX(3000)
        SetScaleY(4200)
        ColorForTransition(2519224570)
    sprite('vrptef_env', 50)
    sprite('vrptef_env', 20)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def pt203_aura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        AddY(-30000)
        AlphaValue(0)
        SetScaleX(5400)
        SetScaleY(1400)
        ColorForTransition(5299310)
    sprite('vrptef_env', 15)
    ConstantAlphaModifier(10)
    sprite('vrptef_env', 5)
    ConstantAlphaModifier(0)
    sprite('vrptef_env', 20)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def pt203_aura3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RenderLayer(2)
        AddY(-11000)
        AlphaValue(0)
        SetScaleX(3200)
        SetScaleY(2000)
        ColorForTransition(15091360)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 10)
    ConstantAlphaModifier(18)
    sprite('vrptef_env', 10)
    ConstantAlphaModifier(0)
    sprite('vrptef_env', 60)
    ConstantAlphaModifier(-20)


@State
def pt203_airaura1():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        RenderLayer(5)
        AddY(8000)
        SetScaleX(3000)
        SetScaleY(4200)
        ColorForTransition(2602452710)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 15)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def pt203_airaura2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        AddY(-30000)
        SetScaleX(5400)
        SetScaleY(1400)
        ColorForTransition(1347476590)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 20)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)


@State
def pt203_airaura3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(3)
        BlendMode_Add()
        AddY(-11000)
        SetScaleX(3200)
        SetScaleY(2000)
        ColorForTransition(1523724930)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 10)
    ConstantAlphaModifier(-30)


@State
def pt203_mahojinsub():

    def upon_IMMEDIATE():
        LinkParticle('ptef_203mahojin')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('null', 70)


@State
def pt203_stick():

    def upon_IMMEDIATE():
        LinkParticle('ptef_203stick')
        BlendMode_Add()
        Size(750)
    sprite('null', 70)


@State
def yugami_ring():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(1400)
    sprite('vr_yugami', 5)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(28000)
    sprite('vr_yugami', 8)
    SetScaleSpeed(100)
    Unknown3059(-2800)


@State
def Atk5DHiWave():

    def upon_IMMEDIATE():
        LinkParticle('ptef_dustB03')
        BlendMode_Add()
        AlphaValue(128)
    sprite('null', 60)


@State
def Atk5DHiquake():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(5)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(100)
        HitOverhead(100)
        Damage(0)
        AttackP1(70)
        Hitstop(0)
        AirPushbackX(6000)
        AirPushbackY(8000)
        HardKnockdown(20)
        SetScaleX(4000)
    sprite('vrdmy_jishin', 1)
    CommonSE('019_quake_1')


@State
def Bomb():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AirUntechableTime(14)
        Hitstun(14)
        BlendMode_Normal()
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        WallCollisionDetection(1)
        AttackLevel_(1)
        Damage(450)
        Hitstop(5)
        EnemyHitstopAddition(0, 7, 7)
        AttackP1(80)
        SingleProration(1)
        StarterRating(2)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_32():
            setGravity(1500)
            physicsXImpulse(9000)
            physicsYImpulse(27000)

        def upon_33():
            setGravity(1500)
            physicsXImpulse(5000)
            physicsYImpulse(27000)

        def upon_34():
            setGravity(1500)
            physicsXImpulse(1000)
            physicsYImpulse(27000)

        def upon_35():
            setGravity(1650)
            physicsXImpulse(12000)
            physicsYImpulse(27000)

        def upon_36():
            setGravity(1500)
            physicsXImpulse(2000)
            physicsYImpulse(28000)

        def upon_37():
            setGravity(1800)
            physicsXImpulse(21000)
            physicsYImpulse(32000)

    def upon_OPPONENT_HIT_OR_BLOCK():
        sendToLabel(0)

    def upon_LANDING():
        sendToLabel(1)
    sprite('vrptef208_bomb00', 32767)
    CreateObject('BombSpark', 0)
    PrivateSE('ptse_06')
    CommonSE('016_explode_0')
    PrivateSE('ptse_01')
    label(0)
    sprite('vrptef208_bomb00', 2)
    CreateObject('BombAttackFire', 1)
    PrivateSE('ptse_26')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_bomb00', 3)
    SetScaleSpeed(60)
    ConstantAlphaModifier(-30)
    sprite('vrptef208_bomb00', 1)
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb00', 2)
    StartMultihit()
    CreateObject('BombFire', -1)
    PrivateSE('ptse_26')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_bomb00', 3)
    StartMultihit()
    SetScaleSpeed(60)
    ConstantAlphaModifier(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb00', 1)
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 20)


@State
def SpBomb():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(1)
        Damage(550)
        BonusProration(110)
        SingleProration(1)
        AirUntechableTime(14)
        Hitstun(14)
        EnemyHitstopAddition(0, 7, 7)
        setGravity(1500)
        physicsXImpulse(12000)
        physicsYImpulse(27000)
        BlendMode_Normal()
        WallCollisionDetection(1)
        AttackP1(80)
        StarterRating(2)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_32():
            setGravity(1500)
            physicsXImpulse(9000)
            physicsYImpulse(27000)

        def upon_33():
            setGravity(1500)
            physicsXImpulse(5000)
            physicsYImpulse(27000)

        def upon_34():
            setGravity(1500)
            physicsXImpulse(1000)
            physicsYImpulse(27000)

        def upon_35():
            setGravity(1650)
            physicsXImpulse(12000)
            physicsYImpulse(27000)

        def upon_36():
            setGravity(1500)
            physicsXImpulse(2000)
            physicsYImpulse(28000)

        def upon_37():
            setGravity(1800)
            physicsXImpulse(21000)
            physicsYImpulse(32000)

    def upon_OPPONENT_HIT_OR_BLOCK():
        sendToLabel(0)

    def upon_LANDING():
        sendToLabel(1)
    SLOT_59 = SLOT_4
    CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef208_bomb01', 32767)
    CreateObject('BombBigSpark', 0)
    PrivateSE('ptse_06')
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    label(0)
    sprite('vrptef208_bomb01', 1)
    CreateObject('SpAttackBombFire', 1)
    CommonSE('016_explode_2')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_bomb01', 3)
    SetScaleSpeed(60)
    ConstantAlphaModifier(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)
    gotoLabel(2)
    loopRest()
    label(1)
    sprite('vrptef208_bomb01', 2)
    StartMultihit()
    CreateObject('SpBombFire', -1)
    CommonSE('016_explode_2')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_bomb01', 3)
    StartMultihit()
    SetScaleSpeed(60)
    ConstantAlphaModifier(-30)
    physicsYImpulse(1500)
    sprite('vrptef208_bomb01', 1)
    StartMultihit()
    gotoLabel(2)
    loopRest()
    label(2)
    sprite('null', 20)


@State
def BombSpark():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        PaletteIndex(1)
        BlendMode_Add()
    label(15)
    sprite('vrptef208_bombspark00', 2)
    sprite('vrptef208_bombspark01', 2)
    gotoLabel(15)


@State
def BombBigSpark():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        E0EAEffectScale(2)
        PaletteIndex(1)
        BlendMode_Add()
    label(15)
    sprite('vrptef208_bombspark00', 2)
    sprite('vrptef208_bombspark01', 2)
    gotoLabel(15)


@State
def BombAttackFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        Damage(800)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        AirUntechableTime(40)
        ChipPercentage(10)
        StarterRating(2)
        UseFireHitspark(1)
        VoodooDamageMultiplier(2)
    sprite('vrdmy_bombfire00', 7)
    StartMultihit()
    CreateParticle('ptef_bombattackfire', 0)
    sprite('vrdmy_bombfire00', 15)


@State
def BombFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        Damage(800)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        AirUntechableTime(40)
        ChipPercentage(10)
        StarterRating(2)
        UseFireHitspark(1)
        VoodooDamageMultiplier(2)
    sprite('vrdmy_bombfire00', 7)
    StartMultihit()
    CreateParticle('ptef_bombDfire', 0)
    sprite('vrdmy_bombfire01', 15)


@State
def SpAttackBombFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(40)
        Damage(1200)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        BonusProration(110)
        ChipPercentage(10)
        UseFireHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        LinkParticle('ptef_bombattackfire')
    sprite('vrdmy_bombfire00', 7)
    StartMultihit()
    Size(1500)
    sprite('vrdmy_bombfire00', 15)


@State
def SpBombFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackY(30000)
        AirUntechableTime(40)
        Damage(1200)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        BonusProration(110)
        ChipPercentage(10)
        UseFireHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        LinkParticle('ptef_bombattackfire')
    sprite('vrdmy_bombfire00', 7)
    StartMultihit()
    Size(1500)
    sprite('vrdmy_bombfire01', 15)


@State
def Missile():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(550)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        PushbackX(10000)
        Hitstop(6)
        ProjectileLevel(2)
        StarterRating(2)
        WallCollisionDetection(1)
        CollideWithWall(1)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_CORNERED():
            sendToLabel(3)
    sprite('vrptef208_missile00', 30)
    CreateObject('MissileBackfire', 0)
    physicsXImpulse(1500)
    CommonSE('016_explode_0')
    PrivateSE('ptse_01')
    sprite('vrptef208_missile00', 150)
    SetAcceleration(4000)
    PrivateSE('ptse_06')
    loopRest()
    label(0)
    sprite('vrptef208_missile00', 30)
    CreateObject('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 150)
    SetAcceleration(4000)
    PrivateSE('ptse_06')
    loopRest()
    label(1)
    sprite('vrptef208_missile00', 50)
    CreateObject('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 130)
    SetAcceleration(4000)
    PrivateSE('ptse_06')
    loopRest()
    label(2)
    sprite('vrptef208_missile00', 70)
    CreateObject('MissileBackfire', 0)
    physicsXImpulse(1500)
    sprite('vrptef208_missile00', 110)
    SetAcceleration(4000)
    PrivateSE('ptse_06')
    loopRest()
    label(3)
    sprite('vrptef208_missile00', 2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(CORNERED)
    CreateObject('MissileFire', -1)
    CommonSE('016_explode_1')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_missile00', 3)
    SetScaleSpeed(80)
    sprite('null', 1)


@State
def SpMissile():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(650)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        BonusProration(110)
        PushbackX(10000)
        Hitstop(6)
        ProjectileLevel(2)
        StarterRating(2)
        AddX(120000)
        WallCollisionDetection(1)
        CollideWithWall(1)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(3)

        def upon_CORNERED():
            sendToLabel(3)
    sprite('vrptef208_missile01', 120)
    CreateObject('MissileBackfire_front', 0)
    CreateObject('MissileBackfire_front', 1)
    CreateObject('MissileBackfire_back', 2)
    physicsXImpulse(40000)
    CommonSE('016_explode_2')
    PrivateSE('ptse_01')
    PrivateSE('ptse_06')
    loopRest()
    label(0)
    sprite('vrptef208_missile01', 30)
    physicsXImpulse(60000)
    CreateObject('MissileBackfire_front', 0)
    CreateObject('MissileBackfire_front', 1)
    CreateObject('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)
    SetAcceleration(4000)
    loopRest()
    label(1)
    sprite('vrptef208_missile01', 30)
    physicsXImpulse(60000)
    CreateObject('MissileBackfire_front', 0)
    CreateObject('MissileBackfire_front', 1)
    CreateObject('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)
    SetAcceleration(4000)
    loopRest()
    label(2)
    sprite('vrptef208_missile01', 10)
    physicsXImpulse(60000)
    CreateObject('MissileBackfire_front', 0)
    CreateObject('MissileBackfire_front', 1)
    CreateObject('MissileBackfire_back', 2)
    sprite('vrptef208_missile01', 60)
    SetAcceleration(4000)
    loopRest()
    label(3)
    sprite('vrptef208_missile01', 1)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    clearUponHandler(CORNERED)
    CreateObject('SpMissileFire', 3)
    CommonSE('016_explode_2')
    physicsXImpulse(0)
    SetAcceleration(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-30)
    sprite('vrptef208_missile01', 3)
    SetScaleSpeed(80)


@State
def MissileFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(40)
        ChipPercentage(10)
        Hitstop(0)
        ProjectileLevel(2)
        VoodooDamageMultiplier(2)
        StarterRating(2)
        UseFireHitspark(1)
    sprite('vrdmy_bombfire02', 10)
    CreateParticle('ptef_missileattackfire', 0)


@State
def SpMissileFire():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(80)
        AttackP2(80)
        SingleProration(1)
        BonusProration(110)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(30000)
        AirUntechableTime(55)
        ChipPercentage(10)
        Hitstop(0)
        ProjectileLevel(2)
        VoodooDamageMultiplier(2)
        UseFireHitspark(1)
        StarterRating(2)
        LinkParticle('ptef_missileattackfire')
    sprite('vrdmy_bombfire02', 10)
    Size(1500)
    sprite('vrdmy_bombfire02', 35)
    StartMultihit()


@State
def MissileBackfire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        Size(1200)
    sprite('vrptef208_missilefire00', 3)
    sprite('vrptef208_missilefire01', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)
    sprite('vrptef208_missilefire00', 3)
    sprite('vrptef208_missilefire01', 3)
    sprite('vrptef208_missilefire02', 3)
    sprite('vrptef208_missilefire00', 3)
    sprite('vrptef208_missilefire01', 3)
    sprite('vrptef208_missilefire02', 3)
    label(15)
    sprite('vrptef208_missilefire00', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)
    CreateParticle('ptef430charge', -1)
    gotoLabel(15)


@State
def MissileBackfire_front():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        Size(1200)
    label(15)
    sprite('vrptef208_missilefire00', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)
    CreateParticle('ptef430charge', -1)
    gotoLabel(15)


@State
def MissileBackfire_back():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        Size(800)
    label(15)
    sprite('vrptef208_missilefire00', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire01', 3)
    CreateParticle('ptef430charge', -1)
    sprite('vrptef208_missilefire02', 3)
    CreateParticle('ptef430charge', -1)
    gotoLabel(15)


@State
def Trap():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        WallCollisionDetection(1)
        BlendMode_Normal()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        NoAttackDuringAction(1)
        HitsPerCall(1, 0, 0, 1, 0, 0, 1, 0)

        def upon_54():
            sendToLabel(2)
            clearUponHandler(54)
            clearUponHandler(LANDING)
        NoDamageAction(1)
        MaxHP(700)
        CurrentHP(700)
        uponSendToLabel(19, 3)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 150000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(1)
        uponSendToLabel(LANDING, 0)
        uponSendToLabel(32, 2)
        uponSendToLabel(53, 2)
    sprite('vrptef209_box00', 32767)
    uponSendToLabel(33, 10)
    uponSendToLabel(34, 20)
    uponSendToLabel(35, 30)
    label(10)
    sprite('vrptef209_box00', 10)
    sprite('vrptef209_box00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    setGravity(1500)
    loopRest()
    label(20)
    sprite('vrptef209_box00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    physicsXImpulse(14000)
    physicsYImpulse(18000)
    setGravity(1500)
    loopRest()
    label(30)
    sprite('vrptef209_box00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    physicsXImpulse(500)
    physicsYImpulse(20000)
    setGravity(1500)
    loopRest()
    label(0)
    sprite('vrptef209_box00', 2)
    AbsoluteY(0)
    EndMomentum(1)
    SetScaleSpeed(-30)
    NoDamageAction(0)
    sprite('vrptef209_box00', 3)
    sprite('vrptef209_box00', 1)
    SetScaleSpeed(0)
    SetActionMark(1)
    loopRest()
    sprite('vrptef209_box00', 719)
    sprite('vrptef209_box00', 1)
    gotoLabel(2)
    label(1)
    sprite('vrptef209_box00', 2)
    NoDamageAction(1)
    sprite('null', 1)
    CreateObject('TrapAttack', 1)
    loopRest()
    ExitState()
    label(2)
    sprite('vrptef209_box00', 2)
    NoDamageAction(1)
    clearUponHandler(EVERY_FRAME)
    EndMomentum(1)
    ConstantAlphaModifier(-10)
    sprite('vrptef209_box00', 10)
    sprite('vrptef209_box00', 10)
    sprite('vrptef209_box00', 10)
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef209_box01', 10)
    NoDamageAction(1)
    EndMomentum(1)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(LANDING)
    clearUponHandler(54)
    PrivateSE('ptse_02')
    CreateParticle('ptef_boxbom', 0)
    ConstantAlphaModifier(-15)
    sprite('vrptef209_box00', 10)


@State
def TrapAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        ChipPercentage(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(40000)
        Damage(1000)
        AttackP1(70)
        AirUntechableTime(55)
        HitAirUnblockable(3)
        StarterRating(2)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef209_box01', 2)
    PrivateSE('ptse_08')
    PrivateSE('ptse_02')
    StartMultihit()
    sprite('vrptef209_box02', 5)
    CreateParticle('ptef_boxbom', 0)
    CreateObject('spring_01', -1)
    sprite('vrptef209_box03', 5)
    CreateObject('spring_02', -1)
    sprite('vrptef209_box04', 5)
    CreateObject('spring_03', -1)
    sprite('vrptef209_box05', 5)
    CreateObject('spring_04', -1)
    sprite('vrptef209_box06', 5)
    sprite('vrptef209_box07', 10)
    ConstantAlphaModifier(-25)
    TriggerUponForState('spring_04', 32)
    sprite('vrptef209_box07', 10)


@State
def spring_01():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring01', 5)


@State
def spring_02():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring02', 5)


@State
def spring_03():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring03', 5)


@State
def spring_04():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        AddX(10000)
        AddY(50000)
        uponSendToLabel(32, 1)
    sprite('vrptef209_spring02', 32767)
    label(1)
    sprite('vrptef209_spring02', 8)
    ConstantAlphaModifier(-31)


@State
def SpTrap():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackP1(80)
        Damage(1000)
        Hitstop(5)
        AirPushbackY(50000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        StarterRating(2)
        WallCollisionDetection(1)
        BlendMode_Normal()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
        NoAttackDuringAction(1)
        NoDamageAction(1)
        MaxHP(1000)
        CurrentHP(1000)
        uponSendToLabel(19, 3)

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_19 < 200000:
                    clearUponHandler(EVERY_FRAME)
                    sendToLabel(1)
        uponSendToLabel(LANDING, 0)
        uponSendToLabel(32, 2)
        uponSendToLabel(53, 2)
    sprite('vrptef209_spbox00', 32767)
    uponSendToLabel(33, 10)
    uponSendToLabel(34, 20)
    uponSendToLabel(35, 30)
    label(10)
    sprite('vrptef209_spbox00', 10)
    sprite('vrptef209_spbox00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    setGravity(1500)
    loopRest()
    label(20)
    sprite('vrptef209_spbox00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    physicsXImpulse(14000)
    physicsYImpulse(18000)
    setGravity(1500)
    loopRest()
    label(30)
    sprite('vrptef209_spbox00', 32767)
    PrivateSE('ptse_01')
    CommonSE('016_explode_0')
    physicsXImpulse(500)
    physicsYImpulse(20000)
    setGravity(1500)
    loopRest()
    label(0)
    sprite('vrptef209_spbox00', 2)
    AbsoluteY(0)
    EndMomentum(1)
    SetScaleSpeed(-30)
    NoDamageAction(0)
    sprite('vrptef209_spbox00', 3)
    sprite('vrptef209_spbox00', 1)
    SetScaleSpeed(0)
    SetActionMark(1)
    loopRest()
    sprite('vrptef209_spbox00', 959)
    sprite('vrptef209_spbox00', 1)
    gotoLabel(2)
    label(1)
    sprite('vrptef209_spbox00', 2)
    NoDamageAction(1)
    CommonSE('016_explode_2')
    SetScaleSpeed(300)
    sprite('null', 3)
    RefreshMultihit()
    CreateObject('Kemuri3', 1)
    CreateObject('SpTrapAttack', 1)
    ExitState()
    label(2)
    sprite('vrptef209_spbox00', 2)
    NoDamageAction(1)
    clearUponHandler(EVERY_FRAME)
    EndMomentum(1)
    ConstantAlphaModifier(-10)
    sprite('vrptef209_spbox00', 10)
    sprite('vrptef209_spbox00', 10)
    sprite('vrptef209_spbox00', 10)
    loopRest()
    ExitState()
    label(3)
    sprite('vrptef209_spbox01', 10)
    NoDamageAction(1)
    EndMomentum(1)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(LANDING)
    clearUponHandler(54)
    PrivateSE('ptse_02')
    CreateParticle('ptef_boxbom', 0)
    ConstantAlphaModifier(-15)
    sprite('vrptef209_spbox00', 10)


@State
def SpTrapAttack():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(900)
        ChipPercentage(10)
        AttackP1(70)
        BonusProration(110)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(50000)
        AirUntechableTime(55)
        HitAirUnblockable(3)
        MinimumDamage(20)
        StarterRating(2)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef209_spbox01', 2)
    PrivateSE('ptse_08')
    PrivateSE('ptse_24')
    StartMultihit()
    sprite('vrptef209_spbox02', 5)
    CreateParticle('ptef_boxbom', 0)
    CreateObject('SPspring_01', -1)
    CreateObject('spbox_parts01', -1)
    CreateObject('spbox_parts02', -1)
    sprite('vrptef209_spbox03', 5)
    CreateObject('SPspring_02', -1)
    sprite('vrptef209_spbox04', 5)
    CreateObject('SPspring_03', -1)
    sprite('vrptef209_spbox05', 5)
    CreateObject('SPspring_04', -1)
    sprite('vrptef209_spbox06', 5)
    sprite('vrptef209_spbox07', 10)
    ConstantAlphaModifier(-25)
    TriggerUponForState('SPspring_04', 32)
    CreateObject('pt209_neko_rocket', -1)
    sprite('null', 30)


@State
def spbox_parts01():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef209_spbox_parts01', 20)
    ConstantAlphaModifier(-12)
    physicsXImpulse(10000)
    physicsYImpulse(30000)
    EndYPhysicsImpulse()


@State
def spbox_parts02():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef209_spbox_parts02', 20)
    ConstantAlphaModifier(-12)
    physicsXImpulse(-10000)
    physicsYImpulse(15000)
    EndYPhysicsImpulse()


@State
def SPspring_01():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        Size(1200)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring01', 5)


@State
def SPspring_02():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        Size(1200)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring02', 5)


@State
def SPspring_03():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        Size(1200)
        AddX(10000)
        AddY(50000)
    sprite('vrptef209_spring03', 5)


@State
def SPspring_04():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AddZVal(1)
        Size(1200)
        AddX(10000)
        AddY(50000)
        uponSendToLabel(32, 1)
    sprite('vrptef209_spring02', 32767)
    label(1)
    sprite('vrptef209_spring02', 8)
    ConstantAlphaModifier(-31)


@State
def pt209_neko_rocket():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        PaletteIndex(0)
        AddY(52000)
        AttackLevel_(3)
        AttackP1(70)
        BonusProration(110)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(50000)
        Damage(800)
        AirUntechableTime(55)
        MinimumDamage(20)
        StarterRating(2)
    sprite('vrptef209_neko_rocket', 2)
    AddX(10000)
    sprite('vrptef209_neko_rocket', 2)
    AddX(-20000)
    sprite('vrptef209_neko_rocket', 2)
    AddX(20000)
    sprite('vrptef209_neko_rocket', 2)
    AddX(-20000)
    sprite('vrptef209_neko_rocket', 2)
    AddX(20000)
    sprite('vrptef209_neko_rocket', 2)
    AddX(-20000)
    sprite('vrptef209_neko_rocket', 5)
    PrivateSE('ptse_06')
    physicsYImpulse(-1000)
    sprite('vrptef209_neko_rocket', 5)
    physicsYImpulse(7000)
    CreateObject('pt209_neko_Backfire', 0)
    CreateObject('pt209_neko_Backfire', 1)
    CreateObject('pt209_neko_Backfire', 2)
    sprite('vrptef209_neko_rocket', 5)
    YAccel(300)
    sprite('vrptef209_neko_rocket', 45)
    YAccel(300)


@State
def pt209_neko_Backfire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleX(800)
        SetScaleY(1200)
        AlphaValue(223)
        RotationAngle(-90000)
        AddY(-57000)
        AddX(-3000)
        LinkParticle('ptef209_rocket_firering')
    label(0)
    sprite('vrptef208_missilefire00', 3)
    CreateParticle('ptef209_rocket', -1)
    sprite('vrptef208_missilefire01', 3)
    CreateParticle('ptef209_rocket', -1)
    sprite('vrptef208_missilefire02', 3)
    CreateParticle('ptef209_rocket', -1)
    gotoLabel(0)


@State
def pt_box():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
    sprite('vrptef209_box00', 32767)
    AddY(224000)
    AddX(224000)
    setGravity(1500)
    CreateParticle('ptef_drivethrow', -1)
    uponSendToLabel(LANDING, 0)
    label(0)
    sprite('vrptef209_box00', 30)
    setGravity(0)
    physicsYImpulse(0)
    sprite('vrptef209_box01', 3)
    sprite('vrptef209_box02', 3)
    CreateParticle('ptef_boxbom', 0)
    sprite('vrptef209_box03', 3)
    sprite('vrptef209_box04', 3)
    sprite('vrptef209_box05', 3)
    sprite('vrptef209_box06', 3)
    sprite('vrptef209_box07', 3)
    sprite('vrptef209_box07', 32)
    ConstantAlphaModifier(-8)


@State
def pt_box2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(0)
    sprite('vrptef209_spbox00', 32767)
    AddY(224000)
    AddX(224000)
    setGravity(1500)
    CreateParticle('ptef_drivethrow', -1)
    uponSendToLabel(LANDING, 0)
    label(0)
    sprite('vrptef209_spbox00', 30)
    setGravity(0)
    physicsYImpulse(0)
    sprite('vrptef209_spbox01', 3)
    sprite('vrptef209_spbox02', 3)
    CreateParticle('ptef_boxbom', 0)
    sprite('vrptef209_spbox03', 3)
    sprite('vrptef209_spbox04', 3)
    sprite('vrptef209_spbox05', 3)
    sprite('vrptef209_spbox06', 3)
    sprite('vrptef209_spbox07', 32)
    ConstantAlphaModifier(-8)


@State
def AirSlideMcirle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('ptef_airspecialmc')
        BlendMode_Add()
    sprite('null', 20)
    AddY(200000)


@State
def AirSlideBalloon():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
    sprite('vrptef401_03', 2)
    AlphaValue(220)
    CreateParticle('ptef_401balloonlight', 0)
    CreateParticle('ptef_401balloonlight', 1)
    CreateParticle('ptef_401balloonlight', 2)
    CreateParticle('ptef_401balloonwave', 1)
    sprite('vrptef401_04', 2)
    sprite('vrptef401_05', 4)


@State
def AssaultAwave():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('ptef_403attack')
        BlendMode_Add()
    sprite('null', 3)
    RotationAngle(20000)
    E0EAEffectPosition(2)
    sprite('null', 30)
    E0EAEffectPosition(0)


@State
def AssaultBwave():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('ptef_403attack')
        BlendMode_Add()
    sprite('null', 3)
    RotationAngle(-20000)
    E0EAEffectPosition(2)
    sprite('null', 30)
    E0EAEffectPosition(0)


@State
def AssaultCwave():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('ptef_403attack')
        BlendMode_Add()
    sprite('null', 3)
    RotationAngle(70000)
    E0EAEffectPosition(2)
    sprite('null', 30)
    E0EAEffectPosition(0)


@State
def CommandThrowMcircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_kousokucircle.DIG', 'ptef_kousokucircle_motion_000.m'
            )
        FaceSpawnLocation()
        BlendMode_Add()
        Size(1100)
        AddY(-40000)
        uponSendToLabel(32, 12)
    sprite('null', 30)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 440)
    AlphaValue(255)
    label(12)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    SetScaleSpeed(25)


@State
def CommandThrowHeart():

    def upon_IMMEDIATE():
        IgnorePauses(22)
        BlendMode_Normal()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef404_00', 3)
    sprite('vrptef404_01', 3)
    sprite('vrptef404_02', 51)
    sprite('vrptef404_02', 6)
    CharacterFlash(16777215, 6, 2)


@State
def CommandThrowRod():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vrptef404_03', 4)
    AlphaValue(255)
    StopCharacterFlash1(16777215)
    CharacterFlash(0, 4, 1)
    sprite('vrptef404_03', 1)


@State
def FakeDoll():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(100)
        SameMoveProration(10)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(100)
        HardKnockdown(10)
        HeatGainMultiplier(1000)
        OppHeatGainMultiplier(0)
        PassByArmor(1)
        OnlyHitPlayer(1)
        StarterRating(2)
        DefeatOpponentBehavior(1)
        DamageEffect(6, 'ptef_hit_low')
        setInvincible(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AttackOff()
    sprite('null', 1)
    if CharacterIDCheck('ha'):
        if random_(2, 0, 35):
            gotoLabel(11)
        gotoLabel(10)
    if CharacterIDCheck('rg'):
        if random_(2, 0, 35):
            gotoLabel(12)
        gotoLabel(10)
    if CharacterIDCheck('hz'):
        if random_(2, 0, 35):
            gotoLabel(13)
        gotoLabel(10)
    if CharacterIDCheck('bn'):
        if random_(2, 0, 35):
            gotoLabel(14)
        gotoLabel(10)
    if CharacterIDCheck('ar'):
        if random_(2, 0, 55):
            gotoLabel(10)
        if random_(2, 0, 60):
            gotoLabel(15)
        if random_(2, 0, 60):
            gotoLabel(16)
        gotoLabel(17)
    gotoLabel(10)
    loopRest()
    label(10)
    sprite('vrptef406_00', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 20)
    sprite('vrptef406_00', 32767)
    RefreshMultihit()
    label(20)
    sprite('vrptef406_00', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_00', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_00', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(11)
    sprite('vrptef406_01', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 21)
    sprite('vrptef406_01', 32767)
    RefreshMultihit()
    label(21)
    sprite('vrptef406_01', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_01', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_01', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(12)
    sprite('vrptef406_02', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 22)
    sprite('vrptef406_02', 32767)
    RefreshMultihit()
    label(22)
    sprite('vrptef406_02', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_02', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_02', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(13)
    sprite('vrptef406_03', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 23)
    sprite('vrptef406_03', 32767)
    RefreshMultihit()
    label(23)
    sprite('vrptef406_03', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_03', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_03', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(14)
    sprite('vrptef406_04', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 24)
    sprite('vrptef406_04', 32767)
    RefreshMultihit()
    label(24)
    sprite('vrptef406_04', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_04', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_04', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(15)
    sprite('vrptef406_05', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 25)
    sprite('vrptef406_05', 32767)
    RefreshMultihit()
    label(25)
    sprite('vrptef406_05', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_05', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_05', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(16)
    sprite('vrptef406_06', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 26)
    sprite('vrptef406_06', 32767)
    RefreshMultihit()
    label(26)
    sprite('vrptef406_06', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_06', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_06', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(17)
    sprite('vrptef406_07', 15)
    AbsoluteY(75000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    StartMultihit()
    SetAcceleration(0)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 27)
    sprite('vrptef406_07', 32767)
    RefreshMultihit()
    label(27)
    sprite('vrptef406_07', 10)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(4000)
    physicsYImpulse(14000)
    sprite('vrptef406_07', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_07', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)


@State
def Atemi_Smoke():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
    sprite('null', 1)
    AddY(150000)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_leaf', -1)
    loopRest()


@State
def DollMaker():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 7)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    sprite('null', 8)
    CreateObject('AttackDoll1', -1)
    label(0)
    sprite('null', 120)
    clearUponHandler(32)


@State
def AttackDoll1():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        TeleportToObject(22)
        AddX(-15000)
        AddY(500000)
        Damage(200)
        AttackType(4)
        AirUntechableTime(100)
        AttackP1(80)
        AttackP2(99)
        MinimumDamage(20)
        Hitstop(0)
        VoodooDamageMultiplier(2)
        StarterRating(2)
        DamageEffect(6, 'ptef_hit_low')
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 1)
    Unknown61(0, 1, 0, 8, 0, 0, 0, 9999, 0, 9999, 0, 9999)
    SLOT_53 = SLOT_0
    if SLOT_53 == 1:
        gotoLabel(11)
    if SLOT_53 == 2:
        gotoLabel(12)
    if SLOT_53 == 3:
        gotoLabel(13)
    if SLOT_53 == 4:
        gotoLabel(14)
    if SLOT_53 == 5:
        gotoLabel(15)
    if SLOT_53 == 6:
        gotoLabel(16)
    if SLOT_53 == 7:
        gotoLabel(17)
    if SLOT_53 == 8:
        gotoLabel(18)
    loopRest()
    label(11)
    sprite('vrptef406_00', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 21)
    label(21)
    sprite('vrptef406_00', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_00', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_00', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(12)
    sprite('vrptef406_01', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 22)
    label(22)
    sprite('vrptef406_01', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_01', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_01', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(13)
    sprite('vrptef406_02', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 23)
    label(23)
    sprite('vrptef406_02', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_02', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_02', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(14)
    sprite('vrptef406_03', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)

    def upon_LANDING():
        StartMultihit()
        SetAcceleration(0)
        physicsXImpulse(0)
        XImpulseAcceleration(90)
        YAccel(90)
        sendToLabel(24)
    label(24)
    sprite('vrptef406_03', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_03', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_03', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(15)
    sprite('vrptef406_04', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 25)
    label(25)
    sprite('vrptef406_04', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_04', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_04', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(16)
    sprite('vrptef406_05', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 26)
    label(26)
    sprite('vrptef406_05', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_05', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_05', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(17)
    sprite('vrptef406_06', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 27)
    label(27)
    sprite('vrptef406_06', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_06', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_06', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()
    label(18)
    sprite('vrptef406_07', 32767)
    CreateParticle('ptef_atemi_smoke', -1)
    CreateParticle('ptef_atemi_doll', -1)
    SetAcceleration(0)
    RandSpeedX(-5000, 5000)
    physicsYImpulse(14000)
    setGravity(700)
    XImpulseAcceleration(90)
    YAccel(90)
    uponSendToLabel(LANDING, 28)
    label(28)
    sprite('vrptef406_07', 20)
    PrivateSE('ptse_00')
    AddRotationPerFrame(-1000)
    physicsXImpulse(-4000)
    physicsYImpulse(14000)
    sprite('vrptef406_07', 5)
    ConstantAlphaModifier(-15)
    sprite('vrptef406_07', 1)
    CreateParticle('ptef_drivethrow', -1)
    CreateParticle('ptef_winsmoke', -1)
    CreateParticle('ptef_winsmoke', -1)
    ExitState()


@State
def pt430_mahojin():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_mahojin2.DIG', 'ptef_mahojin2_motion_000.mmot')
        FaceSpawnLocation()
        RenderLayer(5)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddY(20000)
        Size(800)
    sprite('null', 100)


@State
def ptef_430power():

    def upon_IMMEDIATE():
        LinkParticle('ptef_430power')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
    sprite('null', 45)
    sprite('null', 7)
    ConstantAlphaModifier(-40)


@State
def pt430_circle1():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_circle1.DIG', 'ptef_circle1_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(850)
    sprite('null', 65)


@State
def pt430_circle2():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_circle2.DIG', 'ptef_circle2_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(800)
    sprite('null', 65)


@State
def pt430_mahojinsub():

    def upon_IMMEDIATE():
        LinkParticle('ptef_430mahojin')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 100)


@State
def pt430_aura1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        RenderLayer(5)
        AddY(8000)
        SetScaleX(4000)
        SetScaleY(5600)
        AlphaValue(0)
        ColorForTransition(2642170)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 50)
    ConstantAlphaModifier(-20)


@State
def pt430_aura2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddY(-78000)
        SetScaleX(8500)
        SetScaleY(3000)
        AlphaValue(0)
        ColorForTransition(2657340)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 50)
    ConstantAlphaModifier(-20)


@State
def pt430_aura3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AddY(-11000)
        RenderLayer(5)
        AlphaValue(0)
        SetScaleX(4600)
        SetScaleY(2800)
        ColorForTransition(10490960)
    sprite('vrptef_env', 20)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 50)
    ConstantAlphaModifier(-20)


@State
def pt430_stick():

    def upon_IMMEDIATE():
        LinkParticle('ptef_430stick')
        IgnorePauses(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
    sprite('null', 70)


@State
def pt430_kurukuru():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_kurukuru.DIG', 'ptef_kurukuru_motion_000.mmot')
        FaceSpawnLocation()
        RenderLayer(5)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
    sprite('null', 55)


@State
def ptef_431aura():

    def upon_IMMEDIATE():
        LinkParticle('ptef_431aura')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 70)


@State
def pt431_startcircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_startcircle.DIG', 'ptef_startcircle_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(800)
    sprite('null', 65)


@State
def pt431_floorcircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_floorcircle.DIG', 'ptef_floorcircle_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        RenderLayer(5)
        BlendMode_Add()
        Size(850)
    sprite('null', 180)


@State
def pt431_ranbucircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_ranbucircle.DIG', 'ptef_ranbucircle_motion_000.mmo')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        RenderLayer(5)
        BlendMode_Add()
        AddY(10000)
        Size(700)
    sprite('null', 100)


@State
def pt431_tornado():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_tornado.DIG', 'ptef_tornado_motion_000.mmot')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
        BlendMode_Add()
        AddY(-30000)
        Size(800)
    sprite('null', 100)


@State
def pt431_smoke():

    def upon_IMMEDIATE():
        LinkParticle('ptef_smoke')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        Size(1000)
    sprite('null', 105)
    sprite('null', 20)
    ConstantAlphaModifier(-15)


@State
def pt431_aura1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        AlphaValue(0)
        AbsoluteY(41000)
        SetScaleX(5600)
        SetScaleY(5200)
        ColorForTransition(2629360)
    sprite('vrptef_env', 25)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 43)
    sprite('vrptef_env', 50)
    ConstantAlphaModifier(-20)


@State
def pt431_aura2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        AlphaValue(0)
        AbsoluteY(-51000)
        SetScaleX(4600)
        SetScaleY(3200)
        ColorForTransition(1346620)
    sprite('vrptef_env', 25)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 43)
    sprite('vrptef_env', 50)
    ConstantAlphaModifier(-20)


@State
def pt431_aura3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Add()
        AbsoluteY(-81000)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        AlphaValue(0)
        SetScaleX(5000)
        SetScaleY(3000)
        ColorForTransition(686170)
    sprite('vrptef_env', 15)
    sprite('vrptef_env', 15)
    ConstantAlphaModifier(20)
    sprite('vrptef_env', 40)
    sprite('vrptef_env', 30)
    ConstantAlphaModifier(-10)


@State
def pt440kira():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(130000)
    label(0)
    sprite('null', 4)
    CreateParticle('ptef_440kira_00', -1)
    gotoLabel(0)


@State
def pt440HitEx():

    def upon_IMMEDIATE():
        pass
    sprite('null', 5)
    ParticleSize(1700)
    CallCustomizableParticle('ptef_hit_middle05', -1)
    sprite('null', 5)
    ParticleSize(1700)
    CallCustomizableParticle('ptef_hit_middle05', -1)
    sprite('null', 5)
    ParticleSize(1700)
    CallCustomizableParticle('ptef_hit_middle05', -1)


@State
def Astral1stBeam():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        LinkParticle('ptef_450fast')
        BlendMode_Add()
        uponSendToLabel(32, 12)
    sprite('null', 350)
    label(12)
    sprite('null', 14)
    ConstantAlphaModifier(-20)
    SetScaleXPerFrame(20)
    SetScaleSpeedY(30)


@State
def AstralMcircle():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_kousokucircle.DIG', 'ptef_kousokucircle_motion_000.m'
            )
        FaceSpawnLocation()
        BlendMode_Add()
        Size(1100)
        AddY(-60000)
    sprite('null', 30)
    EffectPosition(22, 103)
    E0EAEffectPosition(22)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('null', 460)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    SetScaleSpeed(15)


@State
def Fade1():
    sprite('vr_fade', 9)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4278190080)
    AlphaValue(0)
    ConstantAlphaModifier(22)
    sprite('vr_fade', 254)
    ConstantAlphaModifier(0)
    sprite('vr_fade', 9)
    ConstantAlphaModifier(-22)


@State
def AstralAura():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        ColorForTransition(16750230)
        uponSendToLabel(32, 13)
    sprite('vrptef_env450_00', 3)
    ConstantAlphaModifier(20)
    AlphaValue(0)
    sprite('vrptef_env450_01', 3)
    sprite('vrptef_env450_02', 3)
    ConstantAlphaModifier(0)
    AlphaValue(200)
    label(15)
    sprite('vrptef_env450_00', 3)
    sprite('vrptef_env450_01', 3)
    sprite('vrptef_env450_02', 3)
    gotoLabel(15)
    label(13)
    sprite('vrptef_env450_00', 10)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(20)


@State
def AstralAura02():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        SetScaleX(6000)
        SetScaleY(6000)
        AddX(10000)
        ColorForTransition(16750230)
        uponSendToLabel(32, 13)
    sprite('vrptef_env', 25)
    ConstantAlphaModifier(9)
    AlphaValue(0)
    sprite('vrptef_env', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    label(13)
    sprite('null', 10)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(20)


@State
def pt450cutin_hand():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        ScreenPosition(1)
        XPositionRelativeFacing(-400000)
        AbsoluteY(-384000)
        Size(400)
    sprite('pt450cutin_00', 4)
    StopCharacterFlash1(16777215)
    SetScaleSpeed(175)
    sprite('pt450cutin_00', 4)
    CreateObject('pt450cutin_hand_par', -1)
    PrivateSE('ptse_13')
    CharacterFlash2(0, 4)
    SetScaleSpeed(0)
    Size(1000)
    sprite('pt450cutin_00', 2)
    StopCharacterFlash2()
    sprite('pt450cutin_00', 27)
    sprite('pt450cutin_00', 3)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-30)
    sprite('pt450cutin_00', 4)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_handbg():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        ScreenPosition(1)
        XPositionRelativeFacing(-400000)
        AbsoluteY(-384000)
        Size(400)
    sprite('vr_pt450cutinbg00', 4)
    StopCharacterFlash1(16777215)
    SetScaleSpeed(175)
    sprite('vr_pt450cutinbg00', 4)
    CharacterFlash2(0, 4)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vr_pt450cutinbg01', 8)
    StopCharacterFlash2()
    sprite('vr_pt450cutinbg02', 8)
    sprite('vr_pt450cutinbg00', 8)
    sprite('vr_pt450cutinbg01', 5)
    sprite('vr_pt450cutinbg01', 3)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-30)
    sprite('vr_pt450cutinbg02', 4)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_hand_par():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        CallPrivateEffect('ptef_450change')
        BlendMode_Add()
        SetPosXByScreenPer(70)
        SetPosYByScreenPer(50)
    sprite('null', 30)
    sprite('null', 6)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_leg():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        ScreenPosition(1)
        XPositionRelativeFacing(-880000)
        AbsoluteY(-384000)
        Size(400)
    sprite('pt450cutin_01', 4)
    StopCharacterFlash1(16777215)
    SetScaleSpeed(175)
    sprite('pt450cutin_01', 4)
    CharacterFlash2(0, 4)
    SetScaleSpeed(0)
    Size(1000)
    CreateObject('pt450cutin_leg_par', -1)
    PrivateSE('ptse_13')
    sprite('pt450cutin_01', 2)
    StopCharacterFlash2()
    sprite('pt450cutin_01', 27)
    sprite('pt450cutin_01', 3)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-30)
    sprite('pt450cutin_01', 4)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_legbg():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        ScreenPosition(1)
        XPositionRelativeFacing(-880000)
        AbsoluteY(-384000)
        Size(400)
    sprite('vr_pt450cutinbg00re', 4)
    StopCharacterFlash1(16777215)
    SetScaleSpeed(175)
    sprite('vr_pt450cutinbg00re', 4)
    CharacterFlash2(0, 4)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vr_pt450cutinbg01re', 8)
    StopCharacterFlash2()
    sprite('vr_pt450cutinbg02re', 8)
    sprite('vr_pt450cutinbg00re', 8)
    sprite('vr_pt450cutinbg01re', 5)
    sprite('vr_pt450cutinbg01re', 3)
    SetScaleSpeed(50)
    ConstantAlphaModifier(-30)
    sprite('vr_pt450cutinbg02re', 4)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_leg_par():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        CallPrivateEffect('ptef_450change')
        BlendMode_Add()
        SetPosXByScreenPer(30)
        SetPosYByScreenPer(50)
    sprite('null', 30)
    sprite('null', 6)
    ConstantAlphaModifier(-40)


@State
def pt450cutin_bustup():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        ScreenPosition(1)
        AbsoluteY(-1200000)
        XPositionRelativeFacingAbsolute(640000)
        SLOT_59 = SLOT_4
        CallPrivateFunction('PT_LinkColor', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('pt450cutin_02', 5)
    StopCharacterFlash1(16777215)
    physicsYImpulse(75000)
    sprite('pt450cutin_03', 5)
    sprite('pt450cutin_04', 5)
    physicsYImpulse(100)
    sprite('pt450cutin_05', 5)
    CharacterFlash2(0, 6)
    CreateObject('pt450cutin_up_par', -1)
    sprite('pt450cutin_02', 1)
    sprite('pt450cutin_02', 4)
    StopCharacterFlash2()
    physicsYImpulse(200)
    sprite('pt450cutin_03', 5)
    PrivateSE('ptse_17')
    sprite('pt450cutin_04', 5)
    sprite('pt450cutin_05', 5)
    physicsYImpulse(400)
    sprite('pt450cutin_06', 5)
    sprite('pt450cutin_07', 5)
    sprite('pt450cutin_08', 5)
    CreateObject('pt450cutin_kira', -1)
    sprite('pt450cutin_09', 5)
    sprite('pt450cutin_10', 5)
    sprite('pt450cutin_11', 5)
    sprite('pt450cutin_08', 5)
    sprite('pt450cutin_09', 5)
    sprite('pt450cutin_10', 5)
    sprite('pt450cutin_11', 5)
    sprite('pt450cutin_08', 5)
    sprite('pt450cutin_09', 5)
    physicsYImpulse(200)
    sprite('pt450cutin_10', 5)
    sprite('pt450cutin_11', 5)
    physicsYImpulse(0)
    sprite('pt450cutin_08', 5)
    sprite('pt450cutin_12', 6)
    TriggerUponForState('pt450cutin_kira', 32)
    AddY(36000)
    sprite('pt450cutin_13', 6)
    physicsYImpulse(3000)
    sprite('pt450cutin_14', 6)
    ConstantAlphaModifier(-20)
    sprite('pt450cutin_15', 6)


@State
def pt450cutin_up_par():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        CallPrivateEffect('ptef_450change')
        BlendMode_Add()
        Size(1200)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 40)
    sprite('null', 20)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(10)


@State
def pt450cutin_kira():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        CallPrivateEffect('ptef_450cutin')
        BlendMode_Add()
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        uponSendToLabel(32, 14)
    sprite('null', 32767)
    label(14)
    sprite('null', 20)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(10)


@State
def pt450cutin_bustupbg():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(0)
        BlendMode_Normal()
        FaceLeft()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-384000)
        XPositionRelativeFacingAbsolute(640000)
    sprite('vr_pt450cutinbg03', 10)
    ConstantAlphaModifier(25)
    AlphaValue(0)
    sprite('vr_pt450cutinbg03', 121)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('vr_pt450cutinbg03', 6)
    ConstantAlphaModifier(-5)
    sprite('vr_pt450cutinbg03', 12)
    ConstantAlphaModifier(-20)


@State
def pt450_mahojin1():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_ahmahojin.DIG', 'ptef_ahmahojin_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
        XPositionRelativeFacing(250000)
        AbsoluteY(250000)
    sprite('null', 20)
    sprite('null', 160)
    sprite('null', 40)
    ConstantAlphaModifier(-15)


@State
def pt450_mahojin2():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_ahmahojin2.DIG', 'ptef_ahmahojin2_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
        XPositionRelativeFacing(200000)
        AbsoluteY(250000)
    sprite('null', 140)


@State
def pt450_mahojin3():

    def upon_IMMEDIATE():
        Eff3DEffect('ptef_ahmahojin3.DIG', 'ptef_ahmahojin3_motion_000.mmot')
        RemoveOnCallStateEnd(2)
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        Size(1000)
        XPositionRelativeFacing(200000)
        AbsoluteY(250000)
    sprite('null', 89)
    sprite('null', 5)
    physicsXImpulse(-5000)
    SetScaleSpeed(40)
    sprite('null', 46)
    physicsXImpulse(-5000)
    SetScaleSpeed(10)


@State
def pt450Beam():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        CallPrivateEffect('ptef_450splash')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
    sprite('null', 16)
    AlphaValue(0)
    sprite('null', 10)
    SetScaleY(0)
    SetScaleSpeedY(110)
    AlphaValue(255)
    physicsXImpulse(-6000)
    sprite('null', 110)
    physicsXImpulse(0)
    SetScaleSpeedY(0)


@State
def FadeWhite():
    sprite('vr_fade', 15)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4294967295)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    sprite('vr_fade', 60)
    ConstantAlphaModifier(0)
    sprite('vr_fade', 15)
    ConstantAlphaModifier(-17)


@State
def AstralAuraWin():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        RenderLayer(5)
        BlendMode_Add()
        SetScaleX(6000)
        SetScaleY(6000)
        AddX(10000)
        ColorFromPaletteIndex(208)
    sprite('vrptef_env', 10)
    ConstantAlphaModifier(18)
    AlphaValue(0)
    sprite('vrptef_env', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(180)


@State
def EntryHeart():

    def upon_IMMEDIATE():
        LinkParticle('ptef_entryheartB')
        BlendMode_Add()
        Size(1000)
    sprite('null', 10)
    sprite('null', 5)
    physicsYImpulse(8000)
    sprite('null', 10)
    physicsYImpulse(10000)
    SetScaleSpeed(10)
    sprite('null', 10)
    SetScaleSpeed(15)
    physicsYImpulse(15000)
    sprite('null', 15)
    physicsYImpulse(20000)


@State
def EntryRod():

    def upon_IMMEDIATE():
        Size(1000)
        AbsoluteY(820000)
        AddX(-85000)
        RotationAngle(100000)
        AddRotationPerFrame(-20000)
        physicsYImpulse(-18200)
        BlendMode_Normal()
    sprite('vrptef601_00', 16)
    CommonSE('008_swing_pole_0')
    sprite('vrptef601_00', 5)
    AddRotationPerFrame(-15000)
    sprite('vrptef601_00', 3)
    AddRotationPerFrame(-12000)


@State
def FusenEntry():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddY(120000)
        XPositionRelativeFacing(-20000)
        BlendMode_Normal()
        AlphaValue(230)
    sprite('vrptef602_09', 6)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef602_08', 8)
    sprite('vrptef602_07', 8)
    sprite('vrptef602_08', 8)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef602_09', 8)
    sprite('vrptef602_10', 8)
    sprite('vrptef602_09', 8)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef602_08', 8)
    sprite('vrptef602_07', 8)
    sprite('vrptef602_08', 8)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef602_09', 8)
    sprite('vrptef602_10', 8)
    sprite('vrptef602_09', 8)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef602_08', 8)
    sprite('vrptef602_07', 8)
    sprite('vrptef602_08', 8)
    sprite('vrptef602_02', 8)
    PrivateSE('ptse_00')
    sprite('vrptef401_04', 6)
    E0EAEffectPosition(0)
    Size(1300)
    ConstantAlphaModifier(-10)
    CommonSE('100_hit_grap_0')
    sprite('vrptef401_05', 6)
    loopRest()


@State
def EventPT01_ibbn():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 1)
        PaletteIndex(7)
        SetZLine(0, 100)
    label(0)
    sprite('bn000_00', 7)
    sprite('bn000_01', 7)
    sprite('bn000_02', 7)
    sprite('bn000_03', 7)
    sprite('bn000_04', 7)
    sprite('bn000_05', 7)
    sprite('bn000_06', 7)
    sprite('bn000_07', 7)
    sprite('bn000_08', 7)
    sprite('bn000_09', 7)
    sprite('bn000_11', 7)
    loopRest()
    gotoLabel(0)
    label(1)
    BlendMode_Normal()
    sprite('bn050_00', 1)
    sprite('bn050_01', 1)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    ConstantAlphaModifier(-10)
    sprite('bn050_02', 30)
    sprite('bn050_02', 5)
    Visibility(1)
    CreateParticle('haef_event_lose', 0)
    CommonSE('014_electric_m')
    CommonSE('001_airbackdash_0')
    sprite('bn050_02', 5)
    ConstantAlphaModifier(0)
    CreateParticle('haef_event_lose_end', 103)
    sprite('bn050_02', 32767)


@State
def ptPhantom():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        AlphaValue(0)
        BlendMode_Normal()
        AddY(70000)
        AddX(-50000)
    sprite('pt999_00', 15)
    ConstantAlphaModifier(10)
    sprite('pt999_00', 6)
    AlphaValue(160)
    ConstantAlphaModifier(0)
    sprite('pt999_00', 120)
    sprite('pt999_00', 6)
    ConstantAlphaModifier(-2)
    physicsXImpulse(-1000)
    sprite('pt999_00', 6)
    physicsXImpulse(-400)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)


@State
def ptPhantom_2():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        AlphaValue(0)
        BlendMode_Normal()
        AddY(70000)
    sprite('pt999_00', 22)
    ConstantAlphaModifier(10)
    sprite('pt999_00', 6)
    ConstantAlphaModifier(0)
    CharacterFlash(3289650, 120, 120)
    uponSendToLabel(32, 1)
    label(0)
    sprite('pt999_00', 50)
    physicsYImpulse(100)
    sprite('pt999_00', 50)
    sprite('pt999_00', 20)
    physicsYImpulse(0)
    sprite('pt999_00', 100)
    physicsYImpulse(-100)
    sprite('pt999_00', 10)
    physicsYImpulse(0)
    gotoLabel(0)
    label(1)
    sprite('pt999_00', 6)
    EndMomentum(1)
    ConstantAlphaModifier(-5)
    physicsXImpulse(-300)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)
    sprite('pt999_00', 6)


@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        TeleportToObject(22)
        AbsoluteY(0)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('null', 1000)
    CameraControlEnable(1)
    CameraNoScreenCollision(1)
    label(1)
    sprite('null', 1)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)


@State
def ptef_408_splash():

    def upon_IMMEDIATE():
        Unknown4022(2)
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
    label(0)
    sprite('null', 3)
    CreateParticle('ptef408splash', -1)
    gotoLabel(0)


@State
def ptef_409_ring():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('vrptef409_01', 3)
    sprite('vrptef409_02', 5)
    sprite('vrptef409_03', 5)
    sprite('vrptef409_04', 2)
    sprite('vrptef409_05', 2)


@State
def ptef_409_ring_air():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
    sprite('vrptef409_14', 3)
    sprite('vrptef409_02ex01', 5)
    sprite('vrptef409_15', 5)
    sprite('vrptef409_16', 2)
    sprite('vrptef409_17', 2)


@State
def BoomerangAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(90)
        AttackP2(79)
        ChipPercentage(10)
        Hitstop(1)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(6)
        AirUntechableTime(55)
        Hitstun(30)
        AirPushbackX(2500)
        AirPushbackY(40000)
        StarterRating(2)
        EnemyHitstopAddition(6, 0, 2)
        ContinueState(300)
        FloorCollision(1)
        WallCollisionDetection(0)
        AddX(-100000)
        AddY(-64000)
        BlendMode_Normal()
        PaletteIndex(0)
        Visibility(1)
        physicsXImpulse(35000)
        SetAcceleration(-500)

        def upon_32():
            SLOT_53 = 1

        def upon_PLAYER_DAMAGED():
            EndAttack()
            AlphaValue(144)
            DespawnEAEffect('Boomerang_blm')
            TriggerUponForState('Boomerang_wing', 33)
            TriggerUponForState('Boomerang_wing_b', 33)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AttackOff()
            AlphaValue(144)
            DespawnEAEffect('Boomerang_blm')
            TriggerUponForState('Boomerang_wing', 33)
            TriggerUponForState('Boomerang_wing_b', 33)

        def upon_EVERY_FRAME():
            XImpulseAcceleration(99)
            if not SLOT_2:
                if SLOT_XVelocity < 10000:
                    SetActionMark(1)
                    sendToLabel(1)
            else:
                ObjectUpon24(23, 100, 3, 100)
                if SLOT_0 < 150000:
                    SetActionMark(0)
                    clearUponHandler(EVERY_FRAME)
                    if not SLOT_53:
                        sendToLabel(2)
                ObjectUpon24(23, 100, 3, 100)
                if SLOT_0 >= 5000000:
                    clearUponHandler(EVERY_FRAME)
    sprite('vrptef409_boomerang', 32767)
    PrivateSE('ptse_30')
    CreateObject('Boomerang_ring', 0)
    CreateObject('Boomerang_wing', 0)
    CreateObject('Boomerang_wing_b', 0)
    CreateObject('Boomerang_pt', 0)
    CreateObject('Boomerang_blm', 0)
    label(1)
    sprite('vrptef409_boomerang', 30)
    SetAcceleration(-300)
    sprite('vrptef409_boomerang', 32767)
    Flip()
    SetAcceleration(1500)
    sprite('keep', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    EndMomentum(1)
    ExitState()
    label(2)
    sprite('keep', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    EndMomentum(1)
    if SLOT_4 == 15:
        SLOT_31 = SLOT_31 + 1
    else:
        ObjectUpon2(3, 0, 0)


@State
def Boomerang_ring():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        Eff3DEffect('ptef_409ring', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        Size(500)
        RenderLayer(7)
    sprite('null', 32767)


@State
def Boomerang_wing():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        RenderLayer(8)

        def upon_33():
            SLOT_51 = 1
            AlphaValue(144)
            ConstantAlphaModifier(-7)
    label(0)
    sprite('vrptef409_wing00', 4)
    sprite('vrptef409_wing01', 4)
    sprite('vrptef409_wing02', 4)
    sprite('vrptef409_wing01', 4)
    if not SLOT_51:
        notConditionalSendToLabel(0)
    sprite('vrptef409_wing00', 4)
    sprite('vrptef409_wing01', 4)
    sprite('vrptef409_wing02', 4)


@State
def Boomerang_wing_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        RenderLayer(6)

        def upon_33():
            SLOT_51 = 1
            AlphaValue(144)
            ConstantAlphaModifier(-7)
    label(0)
    sprite('vrptef409_wing00b', 4)
    sprite('vrptef409_wing01b', 4)
    sprite('vrptef409_wing02b', 4)
    sprite('vrptef409_wing01b', 4)
    if not SLOT_51:
        notConditionalSendToLabel(0)
    sprite('vrptef409_wing00b', 4)
    sprite('vrptef409_wing01b', 4)
    sprite('vrptef409_wing02b', 4)


@State
def Boomerang_blm():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        CallPrivateEffect('ptef409_bloom')
        Size(925)
    sprite('null', 32767)


@State
def Boomerang_pt():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 4)
    CreateParticle('ptef409_light', -1)
    gotoLabel(0)


@State
def SPBoomerangAtk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        ProjectileLevel(2)
        Damage(1100)
        AttackP1(90)
        AttackP2(82)
        BonusProration(110)
        ChipPercentage(10)
        Hitstop(1)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(6)
        AirUntechableTime(60)
        Hitstun(40)
        AirPushbackX(2500)
        AirPushbackY(40000)
        StarterRating(2)
        EnemyHitstopAddition(6, 0, 5)
        BlendMode_Normal()
        PaletteIndex(0)
        Visibility(1)
        ContinueState(300)
        FloorCollision(1)
        WallCollisionDetection(0)
        AddX(-100000)
        AddY(-64000)
        physicsXImpulse(35000)
        SetAcceleration(-500)

        def upon_32():
            SLOT_53 = 1

        def upon_PLAYER_DAMAGED():
            EndAttack()
            AlphaValue(144)
            DespawnEAEffect('Boomerang_blm_sp')
            TriggerUponForState('SPBoomerang_wing', 33)
            TriggerUponForState('SPBoomerang_wing_b', 33)

        def upon_OPPONENT_HIT_OR_BLOCK():
            AttackOff()
            AlphaValue(144)
            DespawnEAEffect('Boomerang_blm_sp')
            TriggerUponForState('SPBoomerang_wing', 33)
            TriggerUponForState('SPBoomerang_wing_b', 33)

        def upon_EVERY_FRAME():
            XImpulseAcceleration(99)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 23)
            PrivateFunction(1, 2, 23, 2, 52, 2, 52)
            PrivateFunction(3, 2, 52, 0, -60, 2, 13)
            if not SLOT_2:
                if SLOT_XVelocity < 10000:
                    SetActionMark(1)
                    sendToLabel(1)
            else:
                ObjectUpon24(23, 100, 3, 100)
                if SLOT_0 < 200000:
                    SetActionMark(0)
                    clearUponHandler(EVERY_FRAME)
                    if not SLOT_53:
                        sendToLabel(2)
                ObjectUpon24(23, 100, 3, 100)
                if SLOT_0 >= 5000000:
                    clearUponHandler(EVERY_FRAME)
    sprite('vrptef409_boomerang_sp', 32767)
    PrivateSE('ptse_30')
    CreateObject('SPBoomerang_ring', 0)
    CreateObject('SPBoomerang_wing', 0)
    CreateObject('SPBoomerang_wing_b', 0)
    CreateObject('Boomerang_pt', 0)
    CreateObject('Boomerang_blm_sp', 0)
    label(1)
    sprite('vrptef409_boomerang_sp', 30)
    SetAcceleration(-300)
    sprite('vrptef409_boomerang_sp', 32767)
    Flip()
    SetAcceleration(1500)
    sprite('keep', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    EndMomentum(1)
    ExitState()
    label(2)
    sprite('keep', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-51)
    EndMomentum(1)
    if SLOT_4 == 16:
        SLOT_31 = SLOT_31 + 1
    else:
        ObjectUpon2(3, 1, 0)


@State
def SPBoomerang_ring():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        Eff3DEffect('ptef_409ring2', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        Size(750)
        RenderLayer(7)
    sprite('null', 32767)


@State
def SPBoomerang_wing():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        RenderLayer(8)

        def upon_33():
            SLOT_51 = 1
            AlphaValue(144)
            ConstantAlphaModifier(-7)
    label(0)
    sprite('vrptef409_sp_wing00', 4)
    sprite('vrptef409_sp_wing01', 4)
    if not SLOT_51:
        notConditionalSendToLabel(0)
    sprite('vrptef409_sp_wing00', 4)
    sprite('vrptef409_sp_wing01', 4)
    sprite('vrptef409_sp_wing00', 4)
    sprite('vrptef409_sp_wing01', 4)


@State
def SPBoomerang_wing_b():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        RenderLayer(6)

        def upon_33():
            SLOT_51 = 1
            AlphaValue(144)
            ConstantAlphaModifier(-7)
    label(0)
    sprite('vrptef409_sp_wing00b', 4)
    sprite('vrptef409_sp_wing01b', 4)
    if not SLOT_51:
        notConditionalSendToLabel(0)
    sprite('vrptef409_sp_wing00b', 4)
    sprite('vrptef409_sp_wing01b', 4)
    sprite('vrptef409_sp_wing00b', 4)
    sprite('vrptef409_sp_wing01b', 4)


@State
def Boomerang_blm_sp():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectDirection(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnContact(2)
        CallPrivateEffect('ptef409_bloom')
        Size(1390)
    sprite('null', 32767)


@State
def Boomerang():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(700)
        HitAirUnblockable(3)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        Visibility(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            DespawnEAEffect('Boomerang_pt')
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_Boomerang', 30)
    CommonSE('008_swing_pole_1')
    CreateObject('Boomerang_ring', 0)
    CreateObject('Boomerang_wing', 0)
    CreateObject('Boomerang_wing_b', 0)
    CreateObject('Boomerang_pt', 0)
    label(10)
    sprite('vr_Boomerang', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('vr_Boomerang', 30)
    StartMultihit()


@State
def SPBoomerang():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        callSubroutine('ItemThrowInit')
        Damage(1000)
        HitAirUnblockable(3)
        setGravity(800)
        physicsXImpulse(26000)
        physicsYImpulse(8000)
        AddRotationPerFrame(7500)
        RandSpeedY(3000, 15000)
        RandSpeedX(-2000, 2000)
        Visibility(1)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            DespawnEAEffect('Boomerang_pt')
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            AttackOff()
            EnableAfterimage(0)
            StopCharacterFlash1(0)
            XImpulseAcceleration(-30)
            physicsYImpulse(20000)
            ExternalForcesRate(0, 0)
            ResetExternalForces()
            AddRotationPerFrame(-10000)
        CancelIfPlayerHit(3)
        uponSendToLabel(LANDING, 1)
    label(0)
    sprite('vr_SPboomerang', 30)
    CommonSE('008_swing_pole_1')
    CreateObject('SPBoomerang_ring', 0)
    CreateObject('SPBoomerang_wing', 0)
    CreateObject('SPBoomerang_wing_b', 0)
    CreateObject('Boomerang_pt', 0)
    label(10)
    sprite('vr_SPboomerang', 30)
    CommonSE('008_swing_pole_1')
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('vr_SPboomerang', 30)
    StartMultihit()


@State
def Act2Event_Camera():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        XPositionRelativeFacing(0)
        AbsoluteY(800000)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(9)
        CameraControlEnable(1)
        RunLoopUpon(17, 2000)
        uponSendToLabel(17, 9)
    sprite('null', 32767)
    CameraNoScreenCollision(1)
    loopRest()
    label(0)
    sprite('null', 32767)
    TeleportToObject(3)
    loopRest()
    label(9)
    sprite('null', 10)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)


@State
def Act2Event_Fade():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AlphaValue(0)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    sprite('null', 60)
    Size(20000)
    ColorForTransition(4278190080)
    ConstantAlphaModifier(4)
    SetBackground(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)


@State
def Act3Event_FadeWhite():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
    sprite('vr_fade', 30)
    BlendMode_Normal()
    Size(20000)
    RenderLayer(3)
    XPositionRelativeFacing(0)
    AbsoluteY(0)
    ScreenPosition(1)
    ColorForTransition(4294967295)
    AlphaValue(0)
    ConstantAlphaModifier(8)
    sprite('vr_fade', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    label(0)
    sprite('vr_fade', 30)
    ConstantAlphaModifier(-8)
