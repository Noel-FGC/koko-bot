@State
def EMB_MU():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_MU.DIG', 'ef_emb_MU_motion_000.mmot')
        RenderLayer(5)
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 20)


@State
def EMB_MU_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_MU.DIG', 'ef_emb_MU_motion_000.mmot')
        RenderLayer(5)
        Visibility(1)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 20)


@State
def EMB_MU_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_MU.DIG', 'ef_emb_MU_motion_000.mmot')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 20)


@Subroutine
def DriveBitReset():
    SetScaleSpeed(0)
    AddRotationPerFrame(0)
    SLOT_61 = 0


@Subroutine
def DriveBitAllDisable():
    SLOT_59 = 0
    SLOT_63 = 0
    SLOT_64 = 1


@State
def DriveBit():

    def upon_IMMEDIATE():
        SLOT_59 = 1
        SLOT_61 = 1
        SLOT_63 = 1
        SLOT_64 = 0
        SLOT_65 = 1
        SLOT_53 = 1
        SLOT_58 = SLOT_OverdriveTimer
        FloorCollision(1)

        def upon_58():
            if EnteredState('ModeFormation5D'):
                AddX(150000)
                AddY(230000)
                XSpeed(15000)
                RotationAngle(0)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormation6D'):
                AddX(150000)
                AddY(230000)
                XSpeed(50000)
                YSpeed(52000)
                RotationAngle(0)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormation4D'):
                AddX(120000)
                AddY(230000)
                XSpeed(-10000)
                YSpeed(50000)
                RotationAngle(0)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormation2D'):
                AddX(150000)
                AddY(230000)
                XSpeed(100000)
                YSpeed(-10000)
                RotationAngle(0)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormationAir5D'):
                AddX(100000)
                AddY(230000)
                XSpeed(15000)
                RotationAngle(10000)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormationAir2D'):
                AddX(100000)
                AddY(230000)
                XSpeed(70000)
                YSpeed(-35000)
                RotationAngle(270000)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormationAir6D'):
                AddX(100000)
                AddY(230000)
                XSpeed(110000)
                YSpeed(-10000)
                RotationAngle(0)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModeFormationAir4D'):
                AddX(100000)
                AddY(230000)
                XSpeed(55000)
                YSpeed(25000)
                RotationAngle(90000)
                if SLOT_58:
                    ForceFaceSprite()
                SLOT_60 = 1
                CreateObject('DriveBitNumber', -1)
                RegisterObject(4, 1)
            if EnteredState('ModePowerUp'):
                SLOT_62 = 1
            if EnteredState('ModeBitAttack'):
                if SLOT_59:
                    sendToLabel(4)
                    SLOT_59 = 0
                    SLOT_65 = 0
            if EnteredState('ModeBitAssault'):
                if SLOT_59:
                    sendToLabel(200)
                    SLOT_59 = 0
                    SLOT_65 = 0
            if EnteredState('ModeBitAssaultOD'):
                if SLOT_59:
                    sendToLabel(250)
                    SLOT_59 = 0
                    SLOT_65 = 0
            if EnteredState('ModeReflection'):
                SLOT_65 = 0
                sendToLabel(100)
            if EnteredState('ModeReflectionOD'):
                SLOT_65 = 0
                sendToLabel(150)
            if EnteredState('ModeUltimateReflection'):
                SLOT_65 = 0
                sendToLabel(500)
            if EnteredState('ModeUltimateReflectionOD'):
                SLOT_65 = 0
                sendToLabel(550)
            if EnteredState('SetNumber1'):
                ObjectGotoState(4, 'SetNumber1', 0)
            if EnteredState('SetNumber2'):
                ObjectGotoState(4, 'SetNumber2', 0)
            if EnteredState('SetNumber3'):
                ObjectGotoState(4, 'SetNumber3', 0)
            if EnteredState('SetNumber4'):
                ObjectGotoState(4, 'SetNumber4', 0)

        def upon_40():
            clearUponHandler(40)
            XImpulseAcceleration(5)
            YAccel(5)
            sendToLabel(201)

        def upon_EVERY_FRAME():
            if not SLOT_57:
                XImpulseAcceleration(88)
                YAccel(88)
                if SLOT_YDistanceFromFloor <= 50000:
                    if not SLOT_YVelocity == 0:
                        YAccel(0)
            if SLOT_53:
                CallPrivateFunction('DriveBitAngleHoming', 0, 20000, 0, 0, 
                    0, 0, 0, 0)
            elif SLOT_58:
                CallPrivateFunction('DriveBitAngleHoming', 0, 12000, 0, 0, 
                    0, 0, 0, 0)
            else:
                CallPrivateFunction('DriveBitAngleHoming', 0, 4000, 0, 0, 0,
                    0, 0, 0)
            if SLOT_42:
                if not SLOT_58:
                    SLOT_63 = 0

        def upon_55():
            if SLOT_57:
                clearUponHandler(55)
                EndMomentum(1)
                sendToLabel(580)

        def upon_LANDING():
            if SLOT_57:
                clearUponHandler(LANDING)
                EndMomentum(1)
                sendToLabel(580)

        def upon_54():
            callSubroutine('DriveBitAllDisable')
            sendToLabel(580)

        def upon_53():
            Unknown23090(23)
    sprite('null', 1)
    sprite('null', 20)
    if SLOT_58:
        SLOT_61 = 1
    CreateObject('BitCreate', 100)
    RegisterObject(5, 1)
    PrivateSE('muse_00')
    sprite('null', 15)
    SLOT_53 = 0
    if SLOT_58:
        sendToLabel(9)
    sprite('null', 45)
    PushSpeedX()
    PushSpeedY()
    Unknown1111(0, 22)
    PopSpeedX()
    PopSpeedY()
    SLOT_61 = 1
    sprite('null', 35)
    SLOT_61 = 0
    sprite('null', 5)
    CreateObject('Eff_DriveBitChange', 100)
    loopRest()
    label(9)
    if not SLOT_62:
        sendToLabel(1)
    sprite('null', 30)
    SLOT_61 = 1
    loopRest()
    gotoLabel(2)
    label(1)
    if not SLOT_63:
        notConditionalSendToLabel(0)
    sprite('null', 1)
    ObjectUpon(5, 32)
    CreateObject('DriveShotStartPointEffect', -1)
    sprite('null', 10)
    CreateObject('BitShot', 100)
    RegisterObject(6, 1)
    CreateObject('BitCore', 100)
    RegisterObject(8, 1)
    SLOT_61 = 0
    sprite('vr_bit00_00', 108)
    Visibility(1)
    if SLOT_63:
        PrivateSE('muse_01')
        CreateObject('DriveBitShot', 100)
        Unknown4055(0)
        CallCustomizableParticle('muef_drivewave', 0)
    sprite('null', 1)
    ObjectUpon(6, 32)
    ObjectUpon(8, 32)
    loopRest()
    gotoLabel(0)
    label(2)
    if not SLOT_63:
        notConditionalSendToLabel(0)
    sprite('null', 1)
    ObjectUpon(5, 32)
    sprite('null', 4)
    CreateObject('BitPowerShot', 100)
    RegisterObject(7, 1)
    CreateObject('BitCore', 100)
    RegisterObject(8, 1)
    sprite('null', 10)
    SLOT_61 = 0
    sprite('null', 104)
    if SLOT_63:
        PrivateSE('muse_02')
        CreateObject('DriveBitPowerShot', 100)
    sprite('null', 1)
    ObjectUpon(CORNERED, 32)
    ObjectUpon(8, 32)
    loopRest()
    gotoLabel(0)
    label(4)
    sprite('null', 3)
    callSubroutine('DriveBitReset')
    callSubroutine('DriveBitAllDisable')
    SLOT_64 = 1
    sprite('null', 10)
    CreateParticle('muef_bitattackmc', 0)
    sprite('null', 1)
    if not SLOT_51:
        PrivateSE('muse_13')
        CreateObject('DriveBitBomb', -1)
    loopRest()
    gotoLabel(580)
    label(100)
    sprite('null', 60)
    callSubroutine('DriveBitAllDisable')
    CreateObject('ReflectionShot', -1)
    CreateObject('ReflectionShotBitPowerChargeEff', -1)
    loopRest()
    gotoLabel(580)
    label(150)
    sprite('null', 60)
    callSubroutine('DriveBitAllDisable')
    CreateObject('ReflectionShotOD', -1)
    CreateObject('ReflectionShotBitPowerChargeEff', -1)
    loopRest()
    gotoLabel(580)
    label(200)
    sprite('null', 5)
    CreateObject('AssaultAtk', -1)
    sprite('null', 10)
    SLOT_61 = 0
    sprite('null', 10)
    ObjectUpon(5, 33)
    sprite('null', 5)
    LinkParticle('muef_440_atkeff')
    sprite('null', 5)
    SLOT_57 = 1
    XSpeed2(1800, 0)
    sprite('null', 4)
    XImpulseAcceleration(1100)
    YAccel(1100)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 50)
    label(201)
    sprite('null', 10)
    sprite('null', 1)
    SLOT_57 = 0
    loopRest()
    gotoLabel(580)
    label(250)
    sprite('null', 5)
    CreateObject('AssaultAtkOD', -1)
    sprite('null', 10)
    SLOT_61 = 0
    sprite('null', 10)
    ObjectUpon(5, 33)
    sprite('null', 5)
    LinkParticle('muef_440_atkeff')
    sprite('null', 5)
    SLOT_57 = 1
    XSpeed2(1800, 0)
    sprite('null', 4)
    XImpulseAcceleration(1100)
    YAccel(1100)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 4)
    XImpulseAcceleration(125)
    YAccel(125)
    sprite('null', 50)
    label(251)
    sprite('null', 10)
    sprite('null', 1)
    SLOT_57 = 0
    loopRest()
    gotoLabel(580)
    label(500)
    sprite('null', 60)
    callSubroutine('DriveBitAllDisable')
    CreateObject('UltimateReflectionShot2nd', -1)
    loopRest()
    gotoLabel(580)
    label(550)
    sprite('null', 60)
    callSubroutine('DriveBitAllDisable')
    CreateObject('UltimateReflectionShot2ndOD', -1)
    loopRest()
    gotoLabel(580)
    label(0)
    sprite('null', 32767)
    callSubroutine('DriveBitReset')
    CreateObject('BitWait', 100)
    RegisterObject(9, 1)
    label(1000)
    sprite('null', 32767)
    callSubroutine('DriveBitReset')
    DeleteObject(9)
    CreateObject('BitWait', 100)
    RegisterObject(9, 1)
    label(580)
    sprite('null', 1)
    CreateParticle('muef_bitkoware', 0)
    sprite('null', 10)
    CreateObject('Eff_KowareYugami', 0)
    callSubroutine('DriveBitReset')
    callSubroutine('DriveBitAllDisable')
    SLOT_64 = 1
    ObjectGotoState(4, 'DeleteNumber', 0)
    sprite('null', 10)
    AlphaValue(255)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    SetScaleXPerFrame(-50)
    ObjectUpon(9, 32)
    ObjectUpon(5, 32)
    sprite('null', 1)
    SetScaleSpeed(0)


@State
def DriveBitNumber():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        RenderLayer(1)
        BlendMode_Normal()

        def upon_58():
            if EnteredState('SetNumber0'):
                sendToLabel(99)
            if EnteredState('SetNumber1'):
                sendToLabel(0)
            if EnteredState('SetNumber2'):
                sendToLabel(1)
            if EnteredState('SetNumber3'):
                sendToLabel(2)
            if EnteredState('SetNumber4'):
                sendToLabel(3)
            if EnteredState('DeleteNumber'):
                sendToLabel(4)
    label(0)
    sprite('null', 151)
    sprite('null', 5)
    sprite('vr_muef_bitno1', 10)
    CreateObject('Bitno', -1)
    CreateParticle('muef_bitnoeff', -1)
    Size(500)
    SetScaleSpeed(50)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vr_muef_bitno1', 32767)
    AlphaValue(255)
    SetScaleSpeed(0)
    Size(1000)
    loopRest()
    label(1)
    sprite('vr_muef_bitno2', 5)
    TriggerUponForState('Bitno', 32)
    CreateObject('Bitno', -1)
    Size(1250)
    SetScaleSpeed(-50)
    sprite('vr_muef_bitno2', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(2)
    sprite('vr_muef_bitno3', 5)
    TriggerUponForState('Bitno', 32)
    CreateObject('Bitno', -1)
    Size(1250)
    SetScaleSpeed(-50)
    sprite('vr_muef_bitno3', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(3)
    sprite('vr_muef_bitno4', 5)
    TriggerUponForState('Bitno', 32)
    CreateObject('Bitno', -1)
    Size(1250)
    SetScaleSpeed(-50)
    sprite('vr_muef_bitno4', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(4)
    sprite('keep', 5)
    ConstantAlphaModifier(-50)
    loopRest()


@State
def DriveBitShot():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(2)
        Damage(500)
        AttackP1(70)
        AttackP2(92)
        BonusProration(110)
        AirUntechableTime(25)
        Hitstop(5)
        AirPushbackY(20000)
        PushbackX(6000)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        CopyFromRightToLeft(23, 2, 1, 2, 2, 1)
        XSpeed2(60000, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                Unknown4055(0)
                CallCustomizableParticle('muef_driveshot', 112)
                ParticleColorFromPalette(241, 240, 241)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
    sprite('null', 1)
    sprite('vr_bit00_00atk', 12)
    if SLOT_42:
        Unknown23090(23)
    Visibility(1)
    SetActionMark(1)
    loopRest()
    label(580)
    sprite('null', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)


@State
def DriveBitPowerShot():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        ProjectileLevel(2)
        Damage(850)
        AttackP1(70)
        AttackP2(92)
        BonusProration(110)
        AirUntechableTime(25)
        PushbackX(6000)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        CopyFromRightToLeft(23, 2, 1, 2, 2, 1)
        XSpeed2(80000, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            if SLOT_2:
                ParticleSize(1000)
                CallCustomizableParticle('muef_5DLaserLight', 103)
                ParticleSize(1000)
                CallCustomizableParticle('muef_5DLaserLight', 112)
                CreateParticle('muef_reflectionshotlightB', 112)
                CreateParticle('muef_reflectionshotlightB', 100)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
        CallPrivateFunction('DriveLaserExInit', 0, 1, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 1, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 1, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('PowerShotHitEffect', 103)
    sprite('null', 1)
    sprite('vr_bit00_00atk', 40)
    if SLOT_42:
        Unknown23090(23)
    LinkParticle('muef_401reflectionshot')
    Visibility(1)
    Visibility(1)
    SetActionMark(1)
    loopRest()
    Unknown23090(23)
    label(580)
    sprite('null', 20)
    ConstantAlphaModifier(-10)
    SetActionMark(0)
    CreateObject('PowerShotHitEffect', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)


@State
def DriveBitBomb():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(700)
        AirUntechableTime(40)
        Hitstop(4)
        PushbackX(8000)
        AttackP1(80)
        SingleProration(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(22000)
        YImpulseBeforeWallbounce(1800)
        AttackDirection(3)
        HitsparkSize(300)
        ReduceHitEffects(1)
        StarterRating(2)
        Visibility(1)
    sprite('null', 1)
    sprite('vr_bit02_00', 3)
    ParticleSize(1650)
    CallCustomizableParticle('muef_bitattack', -1)
    CallPrivateEffect('muef_bitattack')
    Size(1500)
    if SLOT_OverdriveTimer:
        AddScale(300)
    sprite('vr_bit02_00', 3)
    if SLOT_5:
        RefreshMultihit()
    sprite('vr_bit02_00', 3)
    if SLOT_5 >= 2:
        RefreshMultihit()
    PerScale(115)
    sprite('vr_bit02_00', 5)
    if SLOT_5 >= 2:
        RefreshMultihit()
    PerScale(115)
    label(9)
    sprite('vr_bit02_00', 3)
    StartMultihit()
    PerScale(87)
    sprite('vr_bit02_00', 3)
    StartMultihit()
    PerScale(87)
    sprite('vr_bit02_00', 3)
    StartMultihit()
    sprite('vr_bit02_00', 1)
    StartMultihit()


@State
def ReflectionShot_Hontai():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(750)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirUntechableTime(25)
        AirPushbackX(1000)
        PushbackX(1000)
        Hitstop(0)
        EnemyHitstopAddition(6, 6, 8)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackDirection(3)
        AttackOff()
        CallPrivateFunction('ReflectionShotInit', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)

        def upon_LANDING():
            sendToLabel(580)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('muef_401reflectionbit', -1)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_03')
    LinkParticle('muef_401reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(320)
    YAccel(320)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def ReflectionShot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(750)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirUntechableTime(25)
        AirPushbackX(1000)
        PushbackX(1000)
        Hitstop(0)
        EnemyHitstopAddition(6, 6, 8)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackDirection(3)
        AttackOff()
        CallPrivateFunction('ReflectionShotInit', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)

        def upon_LANDING():
            sendToLabel(580)
    sprite('null', 10)
    sprite('null', 10)
    CreateParticle('muef_401reflectionbit', -1)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_03')
    LinkParticle('muef_401reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(320)
    YAccel(320)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def DriveShotStartPointEffect():

    def upon_IMMEDIATE():
        PaletteIndex(2)
    sprite('null', 60)
    CreateParticle('muef_driveshotA', -1)


@State
def PowerShotStartPointEffect():
    sprite('null', 30)
    LinkParticle('muef_Powershot')


@State
def PowerShotHitEffect():
    sprite('null', 21)
    CallCustomizableParticle('muef_Powershothit', 103)


@State
def ReflectionShotPowerChargeEffect():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 42)
    LinkParticle('muef_401charge')
    label(0)
    sprite('null', 12)


@State
def DD_ReflectionShotPowerChargeEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 70)
    CreateParticle('muef_431charge', -1)


@State
def ReflectionShotBitPowerChargeEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ParticleLayer(1)
        BlendMode_Add()
        AlphaValue(0)
        Size(500)
    sprite('vr_mu401ef', 2)
    SetScaleSpeed(75)
    ConstantAlphaModifier(60)
    CreateObject('Eff_ReflectionYugamiRing', -1)
    sprite('vr_mu401ef', 45)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    sprite('vr_mu401ef', 5)
    AlphaValue(120)
    ConstantAlphaModifier(-30)
    SetScaleSpeed(-30)


@State
def ReflectionShotHitEffect():
    sprite('null', 21)
    CreateParticle('muef_401reflectionhit', -1)


@State
def UltimateReflectionShot():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CallPrivateFunction('ReflectionShotInit', 0, 1, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)
        AttackLevel_(4)
        Damage(640)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SameMoveProration(-1)
        AirUntechableTime(40)
        PushbackX(12000)
        Hitstop(0)
        EnemyHitstopAddition(12, 12, 17)
        MinimumDamage(10)
        HitsparkSize(500)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        AttackOff()

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotIdling', 0, 1, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)
        HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
    sprite('null', 1)
    sprite('null', 8)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_03')
    LinkParticle('muef_431reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    PerScaleSpeedX(180)
    PerScaleSpeedY(180)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def UltimateReflectionShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CallPrivateFunction('ReflectionShotInit', 0, 1, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)
        AttackLevel_(4)
        Damage(640)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SameMoveProration(-1)
        AirUntechableTime(40)
        PushbackX(12000)
        Hitstop(0)
        EnemyHitstopAddition(12, 12, 17)
        MinimumDamage(10)
        HitsparkSize(500)
        UseSlashHitspark(1)
        AttackDirection(3)
        AttackType(4)
        StarterRating(2)
        AttackOff()

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotODIdling', 0, 1, 0, 0, 0, 0,
                0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)
        HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
    sprite('null', 1)
    sprite('null', 8)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_01')
    LinkParticle('muef_431reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(120)
    YAccel(120)
    PerScaleSpeedX(180)
    PerScaleSpeedY(180)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def UltimateReflectionShot2nd():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CallPrivateFunction('ReflectionShotInit', 0, 2, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)
        AttackLevel_(4)
        Damage(640)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SameMoveProration(-1)
        AirUntechableTime(40)
        PushbackX(12000)
        Hitstop(0)
        EnemyHitstopAddition(12, 12, 17)
        MinimumDamage(10)
        HitsparkSize(250)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        AttackOff()

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotIdling', 0, 2, 0, 0, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)
        HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
    sprite('null', 1)
    sprite('null', 8)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_03')
    LinkParticle('muef_431reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    PerScaleSpeedX(180)
    PerScaleSpeedY(180)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def UltimateReflectionShot2ndOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        CallPrivateFunction('ReflectionShotInit', 0, 2, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)
        AttackLevel_(4)
        Damage(760)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SameMoveProration(-1)
        AirUntechableTime(40)
        PushbackX(12000)
        Hitstop(0)
        EnemyHitstopAddition(12, 12, 17)
        MinimumDamage(10)
        UseSlashHitspark(1)
        HitsparkSize(250)
        AttackDirection(3)
        StarterRating(2)
        AttackType(4)
        AttackOff()

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotODIdling', 0, 2, 0, 0, 0, 0,
                0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)
        HitsPerCall(1, 0, 0, 0, 0, 0, 0, 0)
        uponSendToLabel(54, 580)

        def upon_LANDING():
            Unknown23090(23)
    sprite('null', 1)
    sprite('null', 8)
    sprite('vr_bit00_00atk', 60)
    PrivateSE('muse_01')
    LinkParticle('muef_431reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(120)
    YAccel(120)
    PerScaleSpeedX(180)
    PerScaleSpeedY(180)
    Visibility(1)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def LaserTest():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        Hitstop(8)
        AttackLevel_(5)
        PushbackX(8000)
        UseSlashHitspark(0)
        UsePunchHitspark(0)
        AttackOff()
        LinkParticle('rgef_drainroop')
        Size(2000)
        Visibility(1)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_16():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)
            if SLOT_2:
                CallCustomizableParticle('muef_reflectionshotlightA', 103)
                CallCustomizableParticle('muef_reflectionshotlightA', 112)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('LaserHit', 103)
            EndMomentum(0)
            sendToLabel(0)
            SetActionMark(0)
            ConstantAlphaModifier(-10)

        def upon_5():
            YAccel(-100)
    sprite('vr_bit00_00atk', 1)
    CreateObject('LaserTestRemain', -1)
    CopyFromRightToLeft(23, 2, 1, 2, 2, 1)
    XSpeed2(52000, 0)
    RefreshMultihit()
    sprite('vr_bit00_00atk', 300)
    SetActionMark(1)
    loopRest()
    label(0)
    sprite('vr_bit00_00atk', 20)


@State
def LaserTestRemain():
    sprite('null', 1)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)


@State
def LaserHit():
    sprite('null', 1)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(2000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(1000)
    CallCustomizableParticle('rcef_birdfire', 103)
    ParticleSize(1000)
    CallCustomizableParticle('rcef_birdfire', 103)
    sprite('null', 1)
    ParticleSize(1000)
    CallCustomizableParticle('noef_AH_flash01', 103)
    sprite('null', 1)
    ParticleSize(1000)
    CallCustomizableParticle('noef_AH_flash01', 103)
    sprite('null', 1)
    ParticleSize(1000)
    CallCustomizableParticle('noef_AH_flash01', 103)


@State
def Funnel6B():
    sprite('mu211_f00', 3)
    physicsXImpulse(3000)
    sprite('mu211_f01', 3)
    sprite('mu211_f02', 3)
    physicsXImpulse(12000)
    sprite('mu211_f03', 2)
    sprite('mu211_f04', 2)
    sprite('mu211_f05', 2)
    sprite('mu211_f06', 2)
    sprite('mu211_f07', 2)
    sprite('mu211_f08', 2)
    sprite('mu211_f09', 2)
    sprite('mu211_f10', 2)
    sprite('mu211_f11', 2)
    physicsXImpulse(8000)
    sprite('mu211_f12', 2)
    sprite('mu211_f13', 2)
    RefreshMultihit()
    sprite('mu211_f14', 3)
    physicsXImpulse(0)
    sprite('mu211_f15', 3)
    sprite('mu211_f16', 3)
    sprite('mu211_f17', 3)
    sprite('mu211_f18', 3)
    sprite('mu211_f19', 3)
    sprite('mu211_f20', 3)
    sprite('mu211_f21', 3)
    sprite('mu211_f22', 3)
    sprite('mu211_f23', 3)


@State
def Funnel3C():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
    sprite('mu234_f00', 2)
    sprite('mu234_f01', 2)
    sprite('mu234_f02', 2)
    sprite('mu234_f03', 1)
    sprite('mu234_f04', 2)
    sprite('mu234_f05', 2)
    sprite('mu234_f06add01', 2)
    sprite('mu234_f07add01', 1)
    sprite('mu234_f08add01', 2)
    sprite('mu234_f09add01', 3)
    sprite('mu234_f10add01', 3)
    sprite('mu234_f11', 3)
    sprite('mu234_f12', 3)
    sprite('mu234_f13', 3)
    sprite('mu234_f14', 3)
    sprite('mu234_f15', 3)
    sprite('mu234_f16', 3)
    sprite('mu234_f17', 3)
    sprite('mu234_f18', 3)


@State
def SwrodSwing_eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AlphaValue(127)
        Size(2000)
        BlendMode_Add()
    sprite('vrmuef404_06', 36)
    CreateObject('SwrodSwing_eff_light', -1)
    sprite('vrmuef404_07', 3)
    sprite('vrmuef404_08', 3)
    sprite('vrmuef404_09', 2)
    AbsoluteY(-64000)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef404_10', 3)
    sprite('vrmuef404_11', 3)
    sprite('vrmuef404_12', 3)


@State
def SwrodSwing_eff10():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AlphaValue(255)
        BlendMode_Add()
    sprite('vrmuef404_07', 2)
    sprite('vrmuef404_08', 2)
    sprite('vrmuef404_09', 3)
    AbsoluteY(-64000)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef404_10', 4)
    sprite('vrmuef404_11', 3)
    sprite('vrmuef404_12', 3)


@State
def SwrodSwing_eff11():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AlphaValue(127)
        BlendMode_Add()
    sprite('vrmuef404_07', 2)
    sprite('vrmuef404_08', 2)
    sprite('vrmuef404_09', 3)
    AbsoluteY(-64000)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef404_10', 4)
    sprite('vrmuef404_11', 3)
    sprite('vrmuef404_12', 3)


@State
def SwrodSwing_eff2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AlphaValue(127)
        BlendMode_Add()
    sprite('vrmuef404_06', 6)
    CreateObject('SwrodSwing_eff_light2', -1)
    sprite('vrmuef404_07', 2)
    sprite('vrmuef404_08', 2)
    sprite('vrmuef404_09', 2)
    AbsoluteY(-64000)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef404_10', 3)
    sprite('vrmuef404_11', 3)
    sprite('vrmuef404_12', 3)


@State
def SwrodSwing_eff_light():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    AlphaValue(0)
    sprite('vrmuef404_06_', 35)
    ConstantAlphaModifier(96)
    CreateObject('SwrodSwing_eff_plazma', 0)
    CreateObject('SwrodSwing_eff_plazma', 1)
    CreateObject('SwrodSwing_eff_plazma', 2)
    CreateObject('SwrodSwing_eff_plazma', 3)
    CreateObject('SwrodSwing_eff_plazma', 4)
    sprite('vrmuef404_07_', 3)
    sprite('vrmuef404_08_', 3)
    sprite('vrmuef404_09_', 2)
    AbsoluteY(-64000)
    sprite('vrmuef404_10_', 3)
    sprite('vrmuef404_11_', 3)
    sprite('vrmuef404_12_', 3)


@State
def SwrodSwing_eff_light_Matome():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        uponSendToLabel(33, 1)
        uponSendToLabel(41, 9)
    label(0)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light11', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light12', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light13', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light14', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light15', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light11', -1)
    CreateObject('SwrodSwing_eff_light11', -1)
    CreateObject('SwrodSwing_eff_light11', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light12', -1)
    CreateObject('SwrodSwing_eff_light12', -1)
    CreateObject('SwrodSwing_eff_light12', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light13', -1)
    CreateObject('SwrodSwing_eff_light13', -1)
    CreateObject('SwrodSwing_eff_light13', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light14', -1)
    CreateObject('SwrodSwing_eff_light14', -1)
    CreateObject('SwrodSwing_eff_light14', -1)
    sprite('null', 1)
    CreateObject('SwrodSwing_eff_light15', -1)
    CreateObject('SwrodSwing_eff_light15', -1)
    CreateObject('SwrodSwing_eff_light15', -1)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('null', 1)


@State
def SwrodSwing_eff_light11():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    ConstantAlphaModifier(320)
    CreateObject('SwrodSwing_eff_plazma11', 0)
    CreateObject('SwrodSwing_eff_plazma11', 1)
    CreateObject('SwrodSwing_eff_plazma11', 2)
    CreateObject('SwrodSwing_eff_plazma11', 3)
    CreateObject('SwrodSwing_eff_plazma11', 4)


@State
def SwrodSwing_eff_light12():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    ConstantAlphaModifier(320)
    CreateObject('SwrodSwing_eff_plazma12', 0)
    CreateObject('SwrodSwing_eff_plazma12', 1)
    CreateObject('SwrodSwing_eff_plazma12', 2)
    CreateObject('SwrodSwing_eff_plazma12', 3)
    CreateObject('SwrodSwing_eff_plazma12', 4)


@State
def SwrodSwing_eff_light13():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    ConstantAlphaModifier(320)
    CreateObject('SwrodSwing_eff_plazma13', 0)
    CreateObject('SwrodSwing_eff_plazma13', 1)
    CreateObject('SwrodSwing_eff_plazma13', 2)
    CreateObject('SwrodSwing_eff_plazma13', 3)
    CreateObject('SwrodSwing_eff_plazma13', 4)


@State
def SwrodSwing_eff_light14():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    ConstantAlphaModifier(320)
    CreateObject('SwrodSwing_eff_plazma14', 0)
    CreateObject('SwrodSwing_eff_plazma14', 1)
    CreateObject('SwrodSwing_eff_plazma14', 2)
    CreateObject('SwrodSwing_eff_plazma14', 3)
    CreateObject('SwrodSwing_eff_plazma14', 4)


@State
def SwrodSwing_eff_light15():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    ConstantAlphaModifier(320)


@State
def SwrodSwing_eff_light20():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_07_', 2)
    sprite('vrmuef404_08_', 2)
    sprite('vrmuef404_09_', 3)
    AbsoluteY(-64000)
    sprite('vrmuef404_10_', 4)
    sprite('vrmuef404_11_', 3)
    sprite('vrmuef404_12_', 3)


@State
def SwrodSwing_eff_light21():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_07_', 2)
    sprite('vrmuef404_08_', 2)
    sprite('vrmuef404_09_', 3)
    AbsoluteY(-64000)
    sprite('vrmuef404_10_', 4)
    sprite('vrmuef404_11_', 3)
    sprite('vrmuef404_12_', 3)


@State
def SwrodSwing_eff_light2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_06_', 1)
    AlphaValue(0)
    sprite('vrmuef404_06_', 5)
    ConstantAlphaModifier(96)
    CreateObject('SwrodSwing_eff_plazma', 0)
    CreateObject('SwrodSwing_eff_plazma', 1)
    CreateObject('SwrodSwing_eff_plazma', 2)
    CreateObject('SwrodSwing_eff_plazma', 3)
    CreateObject('SwrodSwing_eff_plazma', 4)
    sprite('vrmuef404_07_', 2)
    sprite('vrmuef404_08_', 2)
    sprite('vrmuef404_09_', 2)
    AbsoluteY(-64000)
    sprite('vrmuef404_10_', 3)
    sprite('vrmuef404_11_', 3)
    sprite('vrmuef404_12_', 3)


@State
def SwrodSwing_eff_tinkle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('null', 25)
    LinkParticle('muef_404_tinkle')


@State
def SwrodSwing_eff_tinkle2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
    sprite('null', 20)
    LinkParticle('muef_404_tinkle2')


@State
def SwrodSwing_eff_plazma():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    CreateObject('SwrodSwing_eff_tinkle', -1)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)


@State
def SwrodSwing_eff_plazma_NoLink():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    CreateObject('SwrodSwing_eff_tinkle', -1)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    sprite('null', 1)
    sprite('vrmuef404_thd01', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd02', 1)
    sprite('null', 1)
    sprite('vrmuef404_thd03', 1)
    sprite('null', 3)


@State
def SwrodSwing_eff_plazma11():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd00', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)
    CreateObject('SwrodSwing_eff_tinkle', -1)


@State
def SwrodSwing_eff_plazma12():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd01', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)


@State
def SwrodSwing_eff_plazma13():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd02', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)


@State
def SwrodSwing_eff_plazma14():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(2)
        BlendMode_Add()
        PaletteIndex(3)
    sprite('vrmuef404_thd02', 1)
    RandAddScale(-75, 75)
    RandRotationAngle()
    AlphaValue(255)
    ConstantAlphaModifier(-10)
    DeviationX(-3200, 3200)
    DeviationY(-3200, 3200)


@State
def AN_NmlAtkAIR2Cadd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
    sprite('mu253_f02add01', 3)
    sprite('mu253_f03add01', 2)
    sprite('mu253_f04add01', 2)
    sprite('mu253_f05add01', 2)
    sprite('mu253_f06add01', 2)
    sprite('mu253_f07add01', 2)
    sprite('mu253_f08add01', 2)
    sprite('mu253_f09add01', 4)


@State
def AN_NmlAtk6Cadd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(180000)
        AbsoluteY(67000)
    sprite('mu212_f00add01', 1)
    AddX(-128000)
    sprite('mu212_f01add01', 1)
    sprite('mu212_f02add01', 2)
    CreateObject('AN_NmlAtk6C_eff_in', -1)
    CreateObject('AN_NmlAtk6C_eff_in_color', -1)
    sprite('mu212_f03add01', 2)
    sprite('mu212_f04add01', 2)
    sprite('mu212_f05add01', 2)
    sprite('mu212_f06add01', 2)
    sprite('mu212_f07add01', 2)
    sprite('mu212_f08add01', 2)
    CreateObject('AN_NmlAtk6C_eff_out', -1)
    CreateObject('AN_NmlAtk6C_eff_out_color', -1)
    sprite('mu212_f10add02', 10)
    AddX(216000)
    AddY(-8000)
    CreateObject('AN_NmlAtk6C_eff_out_light', -1)
    sprite('mu212_f10add03', 3)
    CreateParticle('muef_212_tinkle', 0)
    sprite('mu212_f10add04', 3)
    sprite('mu212_f10add06', 3)
    sprite('mu212_f10add07', 3)
    sprite('mu212_f10add08', 3)
    sprite('mu212_f12add01', 2)
    AddX(-256000)
    AddY(8000)
    sprite('mu212_f13add01', 3)
    sprite('mu212_f14add01', 3)
    sprite('mu212_f15add01', 3)
    sprite('mu212_f16add01', 4)
    sprite('mu212_f17add01', 4)
    AlphaValue(191)
    sprite('mu212_f18add01', 4)
    AlphaValue(223)


@State
def AN_NmlAtk6C_eff_in():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(-84000)
        AbsoluteY(224000)
        SetPositionZ(1000)
    sprite('null', 54)
    CallPrivateEffect('muef_212_in')
    sprite('null', 1)
    EndObject()
    CreateObject('AN_NmlAtk6C_eff_in_end', -1)


@State
def AN_NmlAtk6C_eff_in_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(-84000)
        AbsoluteY(224000)
        SetPositionZ(1000)
    sprite('null', 8)
    CallPrivateEffect('muef_212_in_end')


@State
def AN_NmlAtk6C_eff_in_color():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(-84000)
        AbsoluteY(224000)
        SetPositionZ(1000)
    sprite('null', 54)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_212_in_color')
    sprite('null', 1)
    EndObject()
    CreateObject('AN_NmlAtk6C_eff_in_color_end', -1)


@State
def AN_NmlAtk6C_eff_in_color_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(-84000)
        AbsoluteY(224000)
        SetPositionZ(1000)
    sprite('null', 8)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_212_in_end_color')


@State
def AN_NmlAtk6C_eff_out():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(394000)
        AbsoluteY(224000)
    sprite('null', 27)
    CallPrivateEffect('muef_212_out')
    sprite('null', 1)
    EndObject()
    CreateObject('AN_NmlAtk6C_eff_out_end', -1)


@State
def AN_NmlAtk6C_eff_out_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(394000)
        AbsoluteY(224000)
    sprite('null', 15)
    CallPrivateEffect('muef_212_out_end')


@State
def AN_NmlAtk6C_eff_out_color():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(434000)
        AbsoluteY(224000)
    sprite('null', 27)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_212_out_color')
    sprite('null', 1)
    EndObject()
    CreateObject('AN_NmlAtk6C_eff_out_color_end', -1)


@State
def AN_NmlAtk6C_eff_out_color_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(434000)
        AbsoluteY(224000)
    sprite('null', 15)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_212_out_end_color')


@State
def AN_NmlAtk6C_eff_out_light():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        IgnorePauses(3)
        XPositionRelativeFacing(434000)
        AbsoluteY(224000)
    sprite('null', 32)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_212_out_swordlight')
    CommonSE('006_swing_blade_2')


@State
def DirectShot_eff():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(3)
        Damage(360)
        PushbackX(9900)
        Hitstop(0)
        AttackP1(80)
        SingleProration(1)
        UseSlashHitspark(1)
        CollideWithWall(1)
        StarterRating(2)
        Unknown12052(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)
            if SLOT_2 == 3:
                sendToLabel(9)
                NoAttackDuringAction(1)
                AttackOff()
                EndAttack()
                clearUponHandler(EVERY_FRAME)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 1)
    CommonSE('014_electric_sl')
    CreateParticle('muef_402_begin', -1)
    sprite('null', 1)
    CreateParticle('muef_402_begin', -1)
    sprite('null', 1)
    CreateParticle('muef_402_begin', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrdmy', 10)
    CommonSE('014_electric_m')
    CreateObject('muef_402_attack', -1)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        SLOT_52 = SLOT_52 + 1
        if SLOT_51 == 4:
            SLOT_51 = 0
            CommonSE('014_electric_m')
            RefreshMultihit()
        if SLOT_52 == 2:
            SLOT_52 = 0
            CreateObject('muef_402_attack', -1)
    sprite('vrdmy', 5)
    XSpeed(20000)
    setGravity(-5)
    sprite('vrdmy', 5)
    XImpulseAcceleration(80)
    sprite('vrdmy', 5)
    XImpulseAcceleration(80)
    sprite('vrdmy', 5)
    XImpulseAcceleration(80)
    sprite('vrdmy', 5)
    setGravity(-200)
    sprite('vrdmy', 5)
    setGravity(-300)
    sprite('vrdmy', 5)
    setGravity(-400)
    sprite('vrdmy', 30)
    setGravity(-500)
    label(9)
    sprite('null', 16)
    CreateParticle('muef_402_end', -1)


@State
def DirectShotAir_eff():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(3)
        Damage(360)
        PushbackX(9900)
        Hitstop(0)
        AttackP1(80)
        SingleProration(1)
        UseSlashHitspark(1)
        StarterRating(2)
        Unknown12052(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            AddActionMark(1)
            if SLOT_2 == 3:
                sendToLabel(9)
                NoAttackDuringAction(1)
                AttackOff()
                EndAttack()
                clearUponHandler(EVERY_FRAME)
                clearUponHandler(LANDING)
        uponSendToLabel(LANDING, 9)
        uponSendToLabel(32, 1)
    label(0)
    RemoveOnCallStateEnd(3)
    sprite('null', 1)
    CommonSE('014_electric_sl')
    CreateParticle('muef_402_begin', -1)
    sprite('null', 1)
    CreateParticle('muef_402_begin', -1)
    sprite('null', 1)
    CreateParticle('muef_402_begin', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    RemoveOnCallStateEnd(0)
    sprite('vrdmy', 40)
    XSpeed(8000)
    YSpeed(2000)
    setGravity(200)
    CommonSE('014_electric_m')
    CreateObject('muef_402_attack', -1)

    def upon_EVERY_FRAME():
        SLOT_51 = SLOT_51 + 1
        SLOT_52 = SLOT_52 + 1
        if SLOT_51 == 4:
            SLOT_51 = 0
            CommonSE('014_electric_m')
        if SLOT_52 == 2:
            SLOT_52 = 0
            CreateObject('muef_402_attack', -1)
            RefreshMultihit()
    sprite('vrdmy', 10)
    XImpulseAcceleration(80)
    sprite('vrdmy', 10)
    XImpulseAcceleration(80)
    label(2)
    sprite('vrdmy', 2)
    gotoLabel(2)
    label(9)
    sprite('null', 46)
    clearUponHandler(EVERY_FRAME)
    CreateParticle('muef_402_end', -1)


@State
def muef_402_attack():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    sprite('null', 10)
    LinkParticle('muef_402_attack')


@State
def GuardCrash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        SetPositionZ(1000)
    sprite('null', 29)
    LinkParticle('muef_407')
    sprite('null', 1)
    EndObject()
    CreateObject('GuardCrash_end', -1)


@State
def GuardCrash_end():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        SetPositionZ(1000)
    sprite('null', 8)
    CallPrivateEffect('muef_407_end')


@State
def GuardCrash_color():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        SetPositionZ(1000)
    sprite('null', 29)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_407_color')
    sprite('null', 1)
    EndObject()
    CreateObject('GuardCrash_end_color', -1)


@State
def GuardCrash_end_color():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
        SetPositionZ(1000)
    sprite('null', 8)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_407_end_color')


@State
def GuardCrash_sword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectDirection(3)
    sprite('null', 100)
    PaletteIndex(0)
    ParticleColorFromPalette(240, 240, 240)
    CallPrivateEffect('muef_407_swordlight')


@State
def UltimateAssaultdmy():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackLevel_(4)
        Damage(400)
        if SLOT_137:
            DamageMultiplier(80)
        Crumple(500)
        Stagger(30)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        IgnoreComboTime(1)
        Hitstop(12)
        DamageFromStateOnly('UltimateAssaultdmy')
        CHStateIfCHStart(3)
        VoodooDamageMultiplier(3)
        TeleportToObject(22)
    sprite('vrdmy_ultimateassault', 1)
    StartMultihit()
    sprite('vrdmy_ultimateassault', 3)


@State
def UltimateAssaultdmy_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        AttackType(4)
        AttackLevel_(4)
        Damage(250)
        if SLOT_137:
            DamageMultiplier(80)
        Crumple(500)
        Stagger(45)
        UseSlashHitspark(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        IgnoreComboTime(1)
        Hitstop(12)
        PushbackX(0)
        DamageFromStateOnly('UltimateAssaultdmy_OD')
        CHStateIfCHStart(3)
        HitsparkSize(400)
        VoodooDamageMultiplier(3)
        TeleportToObject(22)
    sprite('vrdmy_ultimateassault', 1)
    StartMultihit()
    sprite('vrdmy_ultimateassault', 3)


@State
def airBZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(2)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(5)
        PaletteColor2(240)
        PaletteColor3(240)
        PaletteColor4(2147483898)
    sprite('vr_muef251_f00', 3)
    AlphaValue(50)
    ConstantAlphaModifier(75)
    sprite('vr_muef251_f01', 6)
    ConstantAlphaModifier(-50)


@State
def BitCreate():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_newbit_taiki.DIG', '')
        BlendMode_Normal()
        PaletteIndex(2)
        Unknown23122(240)

    def upon_32():
        sendToLabel(3)
        E0EAEffectScale(0)

    def upon_33():
        sendToLabel(1)
        SLOT_51 = 1
        ObjectUpon(FALLING, 33)
    sprite('null', 55)
    CreateObject('Eff_DriveBitCreate', 100)
    RegisterObject(4, 1)
    AlphaValue(0)
    label(1)
    sprite('null', 10)
    clearUponHandler(33)
    ConstantAlphaModifier(50)
    CreateObject('BitCoreTaiki', -1)
    sprite('null', 35)
    ConstantAlphaModifier(0)
    sprite('vr_bit00_01', 150)
    Visibility(1)
    AlphaValue(255)
    if not SLOT_51:
        CreateObject('PowerShotStartPointEffect', 0)
    label(3)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_DriveBitCreate():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('muef_newbitcreate_05')
        BlendMode_Normal()
        uponSendToLabel(33, 1)
    sprite('null', 10)
    Size(750)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    sprite('null', 45)
    ConstantAlphaModifier(0)
    label(1)
    sprite('null', 20)
    clearUponHandler(33)
    CreateParticle('muef_bitstart_02', -1)
    ConstantAlphaModifier(-17)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_DriveBitChange():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('muef_bitchangeA')
        PaletteIndex(2)
    sprite('null', 60)
    ParticleColorFromPalette(240, 241, 242)
    CallCustomizableParticle('muef_bitchangeB', 100)


@State
def BitCore():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_bit_core.DIG', '')
        BlendMode_Normal()
        CallPrivateEffect('muef_bitnomc')
        PaletteIndex(2)
        ColorFromPaletteIndex(242)
    sprite('null', 32767)

    def upon_32():
        sendToLabel(203)
    label(203)
    sprite('null', 1)
    loopRest()


@State
def BitCoreTaiki():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_bit_jizokucore', '')
        CallPrivateEffect('muef_bitnomc')
        BlendMode_Normal()
        PaletteIndex(2)
        ColorFromPaletteIndex(242)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 32767)

    def upon_32():
        sendToLabel(203)
    label(203)
    sprite('null', 1)
    loopRest()


@State
def BitShot():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_newbit_atk.DIG', '')
        AddScale(500)
        BlendMode_Normal()
        RenderLayer(4)
        PaletteIndex(2)
        Unknown23122(240)
    sprite('null', 32767)

    def upon_32():
        sendToLabel(204)
    label(204)
    sprite('null', 1)
    AlphaValue(0)
    loopRest()


@State
def BitPowerShot():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_newbit_atk.DIG', '')
        BlendMode_Normal()
        PaletteIndex(2)
        Unknown23122(240)
    sprite('null', 32767)

    def upon_32():
        sendToLabel(303)
    label(303)
    sprite('null', 1)
    AlphaValue(0)
    loopRest()


@State
def BitWait():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        E0EAEffectDirection(2)
        Eff3DEffect('muef_newbit_taiki.DIG', '')
        BlendMode_Normal()
        PaletteIndex(2)
        Unknown23122(240)
    sprite('null', 32767)
    CreateObject('BitCoreTaiki', -1)

    def upon_32():
        sendToLabel(403)
        E0EAEffectRotation(0)

    def upon_33():
        sendToLabel(403)
    label(403)
    sprite('null', 1)
    AlphaValue(0)
    loopRest()


@State
def Bitno():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('null', 32767)

    def upon_32():
        sendToLabel(503)
    label(503)
    sprite('null', 1)
    AlphaValue(0)
    loopRest()


@State
def Eff_ReflectionYugamiRing():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(1800)
    sprite('vr_yugami01', 5)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami01', 10)
    SetScaleSpeed(100)
    Unknown3059(-3200)


@State
def Eff_KowareYugami():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
    sprite('vr_yugami00', 5)
    SetScaleX(800)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vr_yugami00', 10)
    SetScaleXPerFrame(-120)


@State
def Bit_attackShot():
    sprite('null', 2)
    CreateParticle('muef_bitattackshot03', 2)
    sprite('null', 4)
    PaletteIndex(2)
    CallCustomizableParticle('muef_bitattackshot01', 2)
    ParticleColorFromPalette(240, 241, 240)
    CallCustomizableParticle('muef_bitattackshot02', 2)
    CreateObject('Bit_attackShotYugamiRing', 0)


@State
def Bit_attackShotYugamiRing():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        SetScaleY(1000)
        SetScaleX(450)
    sprite('vr_yugami01', 5)
    SetScaleSpeed(50)
    ParticleTransparency(1)
    PlayerTransparency(32000)
    sprite('vr_yugami01', 10)
    SetScaleSpeed(75)
    Unknown3059(-3200)


@State
def Eff_Drivemc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
    sprite('null', 60)
    CreateParticle('muef_drivemcA', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_drivemc', -1)


@State
def Eff_Driveairmc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
    sprite('null', 60)
    CreateParticle('muef_driveairmcA', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_driveairmc', -1)


@State
def Eff_Driveairmc10():

    def upon_IMMEDIATE():
        PaletteIndex(2)
    sprite('null', 60)
    ParticleSize(1650)
    CreateParticle('muef_driveairmcA', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_driveairmc', -1)


@State
def Eff_mu431mc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
    sprite('null', 60)
    CreateParticle('muef_431mcB', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_431mcA', -1)


@State
def NY_SlowHand():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('muef_431hand', 0)
    CreateParticle('nyef_slowhand01', -1)
    ParticleColorFromPalette(225, 225, 231)
    CallCustomizableParticle('nyef_slowhandcircle00', -1)
    ParticleColorFromPalette(225, 225, 226)


@State
def Eff_FunnelBarrier():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ParticleLayer(1)
        BlendMode_Add()
        AlphaValue(0)
        uponSendToLabel(32, 0)
    sprite('vr_mu403ef', 10)
    PrivateSE('muse_08')
    Size(500)
    SetScaleSpeed(50)
    ConstantAlphaModifier(10)
    sprite('vr_mu403ef', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('vr_mu403ef', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(-50)


@State
def Eff_FunnelBarrierLight():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        ParticleColorFromPalette(65, 66, 65)
        CallPrivateEffect('muef_funnelbarrier')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(0)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    Size(1000)
    SetScaleSpeed(20)
    ConstantAlphaModifier(40)
    sprite('null', 32767)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-20)
    SetScaleSpeed(-50)


@State
def DistortionLockFirst():

    def upon_EVERY_FRAME():
        RemoveOnCallStateEnd(3)
    sprite('vr_mu430_lock00', 1)
    CreateParticle('muef_locksword', 0)
    sprite('vr_mu430_lock01', 1)
    sprite('vr_mu430_lock02', 2)
    sprite('vr_mu430_lock03', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock04', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock05', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock06', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock07', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock08', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock09', 2)
    CreateParticle('muef_locksword_del', 0)
    sprite('vr_mu430_lock10', 2)
    CreateParticle('muef_locksword_del', 0)


@State
def UltimateLockPaticle():

    def upon_IMMEDIATE():
        LinkParticle('muef_locklight')
        RemoveOnCallStateEnd(3)
        TeleportToObject(22)
        AddX(80000)
        AddY(128000)

        def upon_32():
            ConstantAlphaModifier(-40)
    sprite('null', 32767)


@State
def UltimateAtkFunnelA():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(45000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelB():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(65000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(210000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelC():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(75000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(230000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelD():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(85000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(250000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(600)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelE():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(95000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(250000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(600)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelF():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(105000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(230000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelG():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(115000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(210000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def UltimateAtkFunnelH():

    def upon_IMMEDIATE():
        LinkParticle('muef_attacklight')
        RemoveOnCallStateEnd(3)
        RotationAngle(130000)

        def upon_32():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_33():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)

        def upon_34():
            XSpeed2(-1000, 0)
            SetScaleXPerFrame(25)

        def upon_35():
            XSpeed2(200000, 0)
            SetScaleXPerFrame(-100)
            SetScaleSpeedY(450)
            sendToLabel(99)
    sprite('null', 32767)
    label(99)
    sprite('null', 10)


@State
def Eff_ASTFunnel01():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        RenderLayer(2)
        BlendMode_Normal()
    sprite('mu450_f02', 5)
    StopCharacterFlash1(0)
    CharacterFlash2(16777215, 14)
    sprite('mu450_f03', 5)
    sprite('mu450_f04', 5)
    sprite('mu450_f05', 4)
    sprite('mu450_f06', 4)
    sprite('mu450_f07', 5)
    StopCharacterFlash2()
    StopCharacterFlash1(0)


@State
def Eff_ASTSignalmc():

    def upon_IMMEDIATE():
        ParticleLayer(2)
        CallPrivateEffect('muef_ASTattackmc')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(PLAYER_DAMAGED, 99)
    sprite('null', 90)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-4)
    CommonSE('022_magiccircle_c')
    loopRest()
    ExitState()
    label(99)
    sprite('null', 10)
    AlphaValue(100)
    ConstantAlphaModifier(-10)


@State
def ASTLockObj():

    def upon_IMMEDIATE():
        if SLOT_19 > 650000:
            CopyFromRightToLeft(23, 2, 83, 22, 2, 83)
    sprite('null', 30)
    CreateObject('ASTLockObjTop', -1)
    CreateObject('ASTLockObjBottom', -1)


@State
def ASTLockObjTop():

    def upon_IMMEDIATE():
        Eff3DEffect('muef_lockcircle.DIG', 'muef_lockcircle_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(128)
        ContinueState(120)
        uponSendToLabel(32, 99)
        uponSendToLabel(17, 99)
    sprite('null', 10)
    RunLoopUpon(17, 90)
    Size(600)
    physicsYImpulse(44000)
    setGravity(800)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 10)
    SetScaleSpeed(80)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    physicsYImpulse(24000)
    sprite('null', 5)
    SetScaleSpeed(100)
    sprite('null', 5)
    SetScaleSpeed(120)


@State
def ASTLockObjBottom():

    def upon_IMMEDIATE():
        Eff3DEffect('muef_lockcircle.DIG', 'muef_lockcircle_motion_000.mmot')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        AlphaValue(128)
        ContinueState(120)
        uponSendToLabel(32, 99)
        uponSendToLabel(17, 99)
    sprite('null', 10)
    RunLoopUpon(17, 90)
    Size(600)
    physicsYImpulse(10000)
    setGravity(800)
    sprite('null', 32767)
    physicsYImpulse(0)
    setGravity(0)
    label(99)
    sprite('null', 10)
    SetScaleSpeed(80)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    physicsYImpulse(5000)
    sprite('null', 5)
    SetScaleSpeed(100)
    sprite('null', 5)
    SetScaleSpeed(120)


@State
def Eff_ASTFunnel():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ParticleLayer(1)
        BlendMode_Normal()
    UsePunchHitspark(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageInterval(1)
    AfterimageCount(6)
    AfterimageMask_1(0, 0, 0, 128)
    AfterimageMask_2(0, 0, 0, 128)
    AfterimageSize_1(1000)
    AfterimageSize_2(1600)
    sprite('mu450_f10', 6)
    sprite('mu450_f11', 6)
    sprite('mu450_f12', 6)
    sprite('mu450_f13', 6)
    sprite('mu450_f13', 12)
    sprite('mu450_f13', 32767)
    E0EAEffectPosition(22)
    EnableAfterimage(0)


@State
def Eff_ASTFunnelBarrier():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ParticleLayer(1)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 12)
    sprite('vr_mu450ef', 12)
    Size(400)
    SetScaleSpeed(50)
    ConstantAlphaModifier(10)
    sprite('vr_mu450ef', 12)
    SetScaleSpeed(0)
    ConstantAlphaModifier(0)
    Size(1000)
    AlphaValue(128)
    sprite('vr_mu450ef', 32767)
    E0EAEffectPosition(22)


@State
def Eff_ASTFunnelBarrierLight():

    def upon_IMMEDIATE():
        ParticleLayer(4)
        ParticleColorFromPalette(65, 66, 65)
        CallPrivateEffect('muef_funnelbarrier')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        AlphaValue(0)
    sprite('null', 10)
    Size(1000)
    SetScaleSpeed(20)
    ConstantAlphaModifier(40)
    sprite('null', 14)
    SetScaleSpeed(0)
    sprite('null', 32767)
    E0EAEffectPosition(22)


@State
def Eff_ASTbg():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTbgA')
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('null', 16)
    SetScaleY(1200)
    SetScaleX(0)
    SetScaleXPerFrame(40)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    sprite('null', 8)
    SetScaleXPerFrame(20)
    sprite('null', 32767)
    AlphaValue(200)
    AddRotationPerFrame(0)
    SetScaleX(800)
    SetScaleXPerFrame(0)
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_ASTmudammy():
    sprite('mu450_22', 6)
    sprite('mu450_22ex1', 6)
    sprite('mu450_22ex2', 6)
    sprite('mu450_22', 6)
    sprite('mu450_22ex1', 6)
    sprite('mu450_22ex2', 6)
    sprite('mu450_22', 6)
    sprite('mu450_22ex1', 6)
    sprite('mu450_22ex2', 6)


@State
def Eff_ASTChangemc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        E0EAEffectPosition(3)
    sprite('null', 120)
    CreateParticle('muef_ASTmcA', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_ASTmc', -1)


@State
def MU_ASTanime():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-580000)
        XPositionRelativeFacingAbsolute(640000)
        BlendMode_Normal()
        FaceLeft()
    sprite('null', 20)
    sprite('mu451_00', 6)
    sprite('mu451_01', 6)
    sprite('mu451_02', 6)
    sprite('mu451_03', 6)
    CommonSE('000_airdash_1')
    sprite('mu451_04', 6)
    sprite('mu451_05', 6)
    sprite('mu451_06', 6)
    sprite('mu451_07', 6)
    sprite('mu451_08', 6)
    sprite('mu451_09', 6)
    sprite('mu451_10', 6)
    sprite('mu451_11', 6)
    sprite('mu451_12', 6)
    CreateObject('MU_ASTanime_f', -1)
    SetScaleSpeed(-6)
    YSpeed(1100)
    sprite('mu451_13', 6)
    sprite('mu451_14', 6)
    sprite('mu451_15', 4)
    sprite('mu451_16', 4)
    sprite('mu451_17', 4)
    sprite('mu451_18', 4)
    sprite('mu451_19', 4)
    sprite('mu451_20', 4)
    sprite('mu451_21', 4)
    ColorTransition(4291353855, 30)
    PrivateSE('muse_14')
    sprite('mu451_22', 4)
    sprite('mu451_23', 4)
    sprite('mu451_24', 4)
    sprite('mu451_25', 4)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    sprite('mu451_26', 4)
    PerScaleSpeed(40)
    YAccel(40)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    PerScaleSpeed(50)
    YAccel(50)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    PerScaleSpeed(60)
    physicsYImpulse(0)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    SetScaleSpeed(0)
    CommonSE('019_quake_1')
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    PrivateSE('muse_06')
    PrivateSE('muse_06')
    PrivateSE('muse_06')
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    sprite('mu451_26', 4)
    sprite('mu451_27', 4)
    sprite('mu451_28', 4)
    TriggerUponForState('AstralHeat', 32)


@State
def MU_ASTanime_f():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-580000)
        XPositionRelativeFacingAbsolute(640000)
        BlendMode_Normal()
        FaceLeft()
        RenderLayer(5)
    sprite('mu451_f12', 6)
    sprite('mu451_f13', 6)
    sprite('mu451_f14', 6)
    sprite('mu451_f15', 4)
    sprite('mu451_f16', 4)
    sprite('mu451_f17', 4)
    sprite('mu451_f18', 4)
    sprite('mu451_f19', 4)
    sprite('mu451_f20', 4)


@State
def Eff_ASTanimebg():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTbgA')
        RemoveOnCallStateEnd(3)
        RenderLayer(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('null', 36)
    SetScaleXPerFrame(-5)
    sprite('null', 28)
    sprite('null', 32767)
    AlphaValue(255)
    label(0)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_ASTswordmc():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTmcB')
        AddY(-450000)
    sprite('null', 56)
    sprite('null', 4)
    SetScaleX(1200)
    AddY(-36000)
    sprite('null', 4)
    SetScaleX(1200)
    AddY(-26000)
    sprite('null', 4)
    SetScaleX(1500)
    AddY(-29000)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_ASTswordeff():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTswordcharge')
        AddY(-70000)
        AddX(-100000)
        AlphaValue(255)
    sprite('null', 70)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)


@State
def Eff_ASTsword():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTswordlight')
        AddY(-6000)
        AddX(-240000)
    sprite('null', 75)


@State
def Eff_ASTslash():

    def upon_IMMEDIATE():
        CallPrivateEffect('muef_ASTslash')
        FaceLeft()
    sprite('null', 150)
    AddY(-6000)


@State
def FinishWhite():
    sprite('vr_white', 12)
    SetZVal(-500)
    BlendMode_Normal()
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vr_white', 30)
    AlphaValue(255)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def EntryRachel():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        PaletteIndex(7)
        RenderLayer(2)
        BlendMode_Normal()
        IgnorePauses(3)
        CancelIfPlayerHit(3)
    label(0)
    sprite('vr_mu600_00', 6)
    sprite('vr_mu600_01', 6)
    sprite('vr_mu600_02', 6)
    sprite('vr_mu600_03', 6)
    sprite('vr_mu600_04', 6)
    sprite('vr_mu600_05', 6)
    sprite('vr_mu600_06', 6)
    sprite('vr_mu600_07', 6)
    sprite('vr_mu600_08', 6)
    if SLOT_17:
        conditionalSendToLabel(0)
    sprite('vr_mu600_00', 6)
    sprite('vr_mu600_01', 6)
    sprite('vr_mu600_02', 6)
    sprite('vr_mu600_03', 6)
    sprite('vr_mu600_04', 6)
    sprite('vr_mu600_05', 6)
    sprite('vr_mu600_06', 6)
    sprite('vr_mu600_07', 6)
    sprite('vr_mu600_08', 6)
    sprite('vr_mu600_00', 6)
    sprite('vr_mu600_01', 6)
    sprite('vr_mu600_02', 6)
    sprite('vr_mu600_03', 6)
    sprite('vr_mu600_04', 6)
    ConstantAlphaModifier(-15)
    sprite('vr_mu600_05', 6)
    sprite('vr_mu600_06', 6)
    sprite('vr_mu600_07', 6)
    sprite('vr_mu600_08', 6)
    sprite('vr_mu600_00', 6)
    ConstantAlphaModifier(0)


@State
def Eff_Entrymc():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        E0EAEffectPosition(3)
    sprite('null', 120)
    CreateParticle('muef_Entrymc', -1)
    ParticleColorFromPalette(242, 241, 240)
    CallCustomizableParticle('muef_Entrymc00', -1)


@State
def WinSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        SetZVal(500)
        BlendMode_Normal()
    sprite('vr_mu610_f', 15)
    StopCharacterFlash1(16777215)
    CharacterFlash2(0, 15)
    sprite('vr_mu610_f', 32767)
    StopCharacterFlash2()
    StopCharacterFlash1(0)


@State
def RLAstSmoke():

    def upon_IMMEDIATE():
        LinkParticle('muef_rlAHsmoke')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 65)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def muef406_blade():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
    sprite('vrmuef406_00', 1)
    sprite('vrmuef406_01', 1)
    sprite('vrmuef406_02', 5)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef406_03', 2)
    sprite('vrmuef406_04', 3)
    sprite('vrmuef406_05', 3)
    sprite('vrmuef406_06', 3)
    PaletteIndex(0)
    BlendMode_Normal()


@State
def muef406_blade_light():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef406_00_', 1)
    sprite('vrmuef406_01_', 1)
    sprite('vrmuef406_02_', 5)
    sprite('vrmuef406_03_', 2)
    sprite('vrmuef406_04_', 3)
    sprite('vrmuef406_05_', 3)
    sprite('null', 3)


@State
def GuardCrushFunnel():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        CancelIfPlayerHit(3)
    sprite('mu407_f02', 3)
    sprite('mu407_f03', 3)
    CreateParticle('muef_407_tinkle', 0)
    sprite('mu407_f04', 3)
    sprite('mu407_f05', 2)
    sprite('mu407_f06', 2)


@State
def AST_Sword():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(5)
        DefeatOpponentBehavior(1)
        AbsoluteY(2000000)
        XPositionRelativeFacing(0)
        DeviationX(-1000000, 1000000)
        Size(3000)
        RotationAngle(180000)
        Visibility(1)
    sprite('vr_bossmu404_02', 60)
    RefreshMultihit()
    physicsYImpulse(-100000)
    setGravity(3000)

    def upon_LANDING():
        sendToLabel(1)
    label(1)
    sprite('vr_bossmu404_02', 20)
    EndMomentum(1)
    ConstantAlphaModifier(-25)


@State
def AHsumonsordMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        AddX(0)
    sprite('null', 20)
    CreateObject('AHfannelray00', -1)
    CreateObject('AHfannelray', -1)

    def RunOnObject_1():
        AddY(300000)
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(150000)
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(150000)
        AddY(-150000)
        Rotation(45000)
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(150000)
        AddY(150000)
        Rotation(-45000)
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddY(-150000)
        Rotation(90000)
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(-150000)
        Flip()
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(-150000)
        AddY(-150000)
        Rotation(45000)
        Flip()
    sprite('null', 1)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddX(-150000)
        AddY(150000)
        Rotation(-45000)
        Flip()
    sprite('null', 120)
    CreateObject('AHsumonsord00', -1)

    def RunOnObject_1():
        AddY(150000)
        Rotation(-90000)


@State
def AHsumonsord00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_AHsord00', '')
        BlendMode_Normal()
        AlphaValue(0)
        AddScale(500)
        AddY(150000)
    sprite('null', 15)
    ConstantAlphaModifier(17)
    sprite('null', 105)


@State
def AHfannelray():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        BlendMode_Add()
        PaletteIndex(1)
        RenderLayer(2)
        AddY(-50000)
        Size(1000)
        FaceLeft()
        AlphaValue(0)
        EnableAfterimage(1)
        AfterimageInterval(1)
        AfterimageCount(15)
        AfterimageSize_2(1200)
    sprite('vrmuef451_fannelray', 4)
    SetScaleSpeed(8)
    ConstantAlphaModifier(51)
    AddRotationPerFrame(-2000)
    sprite('vrmuef451_fannelray', 4)
    sprite('vrmuef451_fannelray', 20)
    SetScaleSpeed(50)
    sprite('vrmuef451_fannelray', 30)
    ConstantAlphaModifier(-9)
    EndMomentum(1)


@State
def AHfannelray00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(180000)
    sprite('null', 32767)
    LinkParticle('muef_AHsumonray_add')
    EndMomentum(1)


@State
def AHskyray():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(100000)
    sprite('null', 90)
    SetScaleSpeed(1)
    LinkParticle('muef_AHskyray00')
    sprite('null', 50)
    ConstantAlphaModifier(-5)


@State
def AHsumonsord01Matome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectRotation(2)
        BlendMode_Normal()
        AlphaValue(255)
        IgnoreScreenfreeze(1)
    sprite('null', 20)
    CreateObject('AHsumonsord01', -1)

    def RunOnObject_1():
        Flip()
        SetScaleZ(200)
        AddX(700000)
    ScreenShake(10000, 10000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    sprite('null', 15)
    CreateObject('AHsumonsord01', -1)

    def RunOnObject_1():
        SetScaleZ(400)
    ScreenShake(10000, 10000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    sprite('null', 15)
    CreateObject('AHsumonsord01', -1)

    def RunOnObject_1():
        Flip()
        SetScaleZ(600)
    ScreenShake(20000, 20000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    AddCombo(1)
    sprite('null', 15)
    CreateObject('AHsumonsord01', -1)

    def RunOnObject_1():
        SetScaleZ(700)
        AddX(700000)
    ScreenShake(20000, 20000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    AddCombo(1)
    sprite('null', 30)
    CreateObject('AHsumonsord01', -1)
    ScreenShake(20000, 20000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    sprite('null', 15)
    CreateObject('AHsumonsord02', -1)
    ScreenShake(80000, 80000)
    CommonSE('015_blaze_0')
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    CommonSE('015_blaze_0')
    PrivateSE('muse_12')
    AddCombo(1)
    sprite('null', 200)
    LinkParticle('muef_AHwhiteout_00')


@State
def AHsumonsord01():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_AHsord01.DIG', 'muef_AHsord01.mmot')
        BlendMode_Normal()
        AlphaValue(255)
    sprite('null', 20)
    sprite('null', 100)
    LinkParticle('muef_AHsordhit_00')
    ScreenShake(20000, 20000)
    AddCombo(1)


@State
def AHsumonsord02():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_AHsord02.DIG', '')
        BlendMode_Normal()
        AlphaValue(255)
    sprite('null', 20)
    sprite('null', 100)
    LinkParticle('muef_AHsordhit_00')
    ScreenShake(40000, 40000)
    AddCombo(1)


@State
def AHbom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        Eff3DEffect('muef_AHbom.DIG', '')
        BlendMode_Normal()
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 59)


@State
def AHfinishBG():

    def upon_IMMEDIATE():
        Eff3DEffect('muef_AHsord03', '')
        BlendMode_Normal()
        FaceRight()
    sprite('null', 32767)


@State
def SummonNoel():

    def upon_IMMEDIATE():
        PaletteIndex(6)
    label(0)
    sprite('no000_00', 7)
    sprite('no000_01', 7)
    sprite('no000_02', 7)
    sprite('no000_03', 7)
    sprite('no000_04', 7)
    sprite('no000_05', 7)
    sprite('no000_06', 7)
    sprite('no000_07', 7)
    loopRest()
    gotoLabel(0)


@State
def BurstDDAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackOff()
        PrivateSE('muse_14')
        AttackLevel_(5)
        Damage(2430)
        AttackType(4)
        AttackP2(100)
        MinimumDamage(0)
        AirPushbackX(-1000)
        HardKnockdown(60)
        SingleProration(1)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirUntechableTime(60)
        UseFireHitspark(1)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        DamageFromStateOnly('BurstDDAtk')
        CHStateIfCHStart(3)
        OnlyHitPlayer(1)
        TeleportToObject(22)
        AbsoluteY(180000)
        physicsYImpulse(200)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(34)
            sendToLabel(2)

        def upon_34():
            clearUponHandler(34)
            sendToLabel(3)

        def upon_35():
            clearUponHandler(35)
            if SLOT_2:
                sendToLabel(5)
            else:
                sendToLabel(4)

        def upon_41():
            clearUponHandler(41)
            SetActionMark(1)
    sprite('mu440_f10', 5)
    AlphaValue(0)
    ConstantAlphaModifier(28)
    sprite('mu440_f11', 5)
    sprite('mu440_f12', 5)
    label(0)
    sprite('mu440_f10', 5)
    sprite('mu440_f11', 5)
    sprite('mu440_f12', 5)
    gotoLabel(0)
    label(1)
    PaletteIndex(3)
    EnableAfterimage(1)
    AfterimageCount(3)
    sprite('vrmuef440_00', 3)
    sprite('vrmuef440_01', 3)
    sprite('vrmuef440_02', 3)
    gotoLabel(1)
    label(2)
    sprite('vrmuef440_00', 2)
    sprite('vrmuef440_01', 2)
    sprite('vrmuef440_02', 2)
    gotoLabel(2)
    label(3)
    sprite('vrmuef440_00', 2)
    sprite('vrmuef440_01', 2)
    sprite('vrmuef440_02', 2)
    gotoLabel(3)
    label(4)
    sprite('vrmuef440_02', 2)
    sprite('vrmuef440_20', 2)
    sprite('vrmuef440_20', 2)
    AddScale(-150)
    sprite('vrmuef440_21', 3)
    AddScale(150)
    EnableAfterimage(0)
    sprite('vrmuef440_22', 8)
    physicsYImpulse(-20000)
    CameraPosition(1300)
    sprite('vrmuef440_22', 2)
    physicsYImpulse(0)
    sprite('vrmuef440_22', 15)
    CreateObject('BurstDDEff', -1)
    RefreshMultihit()
    Visibility(1)
    AirPushbackY(90000)
    YImpulseBeforeWallbounce(3000)
    AirUntechableTime(120)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 30)
    sprite('null', 10)
    TriggerUponForState('BurstDDEff', 32)
    CameraPosition(1000)
    sprite('null', 10)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    sprite('null', 10)
    ExitState()
    label(5)
    sprite('vrmuef440_02', 2)
    sprite('vrmuef440_20', 2)
    sprite('vrmuef440_20', 2)
    AddScale(-150)
    sprite('vrmuef440_21', 3)
    AddScale(150)
    EnableAfterimage(0)
    sprite('vrmuef440_22', 8)
    physicsYImpulse(-20000)
    CameraPosition(1300)
    sprite('vrmuef440_22', 2)
    physicsYImpulse(0)
    sprite('vrmuef440_22', 4)
    CreateObject('BurstDDEffEX', -1)
    RefreshMultihit()
    Visibility(1)
    Damage(525)
    AirPushbackY(20000)
    Hitstop(2)
    AirUntechableTime(120)
    DefeatOpponentBehavior(1)
    CommonSE('016_explode_2')
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    sprite('vrmuef440_22', 4)
    RefreshMultihit()
    DefeatOpponentBehavior(0)
    AirPushbackY(65000)
    YImpulseBeforeWallbounce(3000)
    CommonSE('016_explode_2')
    CommonSE('016_explode_2')
    sprite('null', 30)
    sprite('null', 10)
    TriggerUponForState('BurstDDEffEX', 32)
    CameraPosition(1000)
    sprite('null', 10)
    CameraControlEnable(0)
    CameraNoScreenCollision(0)
    sprite('null', 10)
    ExitState()


@State
def BurstDDEffEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('muef_440hasira00', '')
        SetScaleY(0)
        uponSendToLabel(32, 0)
        RemoveOnCallStateEnd(2)
    sprite('null', 2)
    CreateObject('BurstDDEffroot', -1)

    def RunOnObject_1():
        AddScale(500)
        AddY(-75000)
    SetScaleSpeedY(100)
    SetScaleXPerFrame(-20)
    SetScaleSpeedZ(-20)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(40000, 40000)
    sprite('null', 2)
    ScreenShake(40000, 40000)
    sprite('null', 2)
    ScreenShake(40000, 40000)
    sprite('null', 2)
    ScreenShake(40000, 40000)
    sprite('null', 32767)
    SetScaleSpeedY(0)
    SetScaleXPerFrame(0)
    SetScaleSpeedZ(0)
    CreateObject('BurstDDEff_Circle', -1)

    def RunOnObject_1():
        AddScale(200)
    CreateObject('BurstDDEff_minicrossMatoEX', -1)
    CreateObject('BurstDDEffsub', -1)

    def RunOnObject_1():
        AddY(600000)
        AddScale(200)
        Rotation(-5000)
    CreateObject('BurstDDEffsub', -1)

    def RunOnObject_1():
        AddY(600000)
        AddScale(200)
        Rotation(-5000)
        Flip()
    label(0)
    sprite('null', 10)
    ParticleLayer(4)
    CallCustomizableParticle('muef_440_whiteout', -1)
    TriggerUponForState('BurstDDEffsub', 32)
    TriggerUponForState('BurstDDEff_minicrossMatoEX', 32)
    SetScaleSpeedY(50)
    SetScaleXPerFrame(-50)
    SetScaleSpeedZ(-50)


@State
def BurstDDEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('muef_440hasira00', '')
        SetScaleY(0)
        uponSendToLabel(32, 0)
        RemoveOnCallStateEnd(2)
    sprite('null', 2)
    CreateObject('BurstDDEffroot', -1)
    SetScaleSpeedY(100)
    SetScaleXPerFrame(-40)
    SetScaleSpeedZ(-40)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 2)
    ScreenShake(20000, 20000)
    sprite('null', 32767)
    SetScaleSpeedY(0)
    SetScaleXPerFrame(0)
    SetScaleSpeedZ(0)
    CreateObject('BurstDDEff_Circle', -1)
    CreateObject('BurstDDEff_minicrossMato', -1)
    CreateObject('BurstDDEffsub', -1)

    def RunOnObject_1():
        AddY(600000)
    CreateObject('BurstDDEffsub', -1)

    def RunOnObject_1():
        AddY(600000)
        Flip()
    label(0)
    sprite('null', 10)
    ParticleLayer(4)
    CallCustomizableParticle('muef_440_whiteout', -1)
    TriggerUponForState('BurstDDEffsub', 32)
    TriggerUponForState('BurstDDEff_minicrossMato', 32)
    SetScaleSpeedY(50)
    SetScaleXPerFrame(-50)
    SetScaleSpeedZ(-50)


@State
def BurstDDEffsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('muef_440hasira00', '')
        SetScaleX(300)
        SetScaleZ(300)
        SetScaleY(0)
        RotationAngle(90000)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 5)
    SetScaleSpeedY(35)
    SetScaleXPerFrame(-12)
    SetScaleSpeedZ(-12)
    sprite('null', 2)
    sprite('null', 2)
    label(0)
    sprite('null', 2)
    SetScaleSpeedY(0)
    SetScaleXPerFrame(0)
    SetScaleSpeedZ(0)
    AddScaleY(100)
    sprite('null', 2)
    AddScaleY(-100)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    SetScaleSpeedY(-10)
    SetScaleXPerFrame(-15)
    SetScaleSpeedZ(-15)


@State
def BurstDDEffroot():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('muef_440_root')
        RemoveOnCallStateEnd(2)
    sprite('null', 32767)


@State
def BurstDDEff_minicrossMatoEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(100000)
        AddY(100000)
        Rotation(10000)
        Size(1100)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(-230000)
        AddY(100000)
        Rotation(-10000)
        Size(1500)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(275000)
        AddY(100000)
        Rotation(25000)
        Size(1900)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(-275000)
        AddY(100000)
        Rotation(-25000)
        Size(1100)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(350000)
        AddY(100000)
        Rotation(30000)
        Size(1300)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(450000)
        AddY(-200000)
        Rotation(30000)
        Size(4000)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(-500000)
        AddY(-200000)
        Rotation(-30000)
        Size(4000)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(550000)
        AddY(-400000)
        Rotation(30000)
        Size(2500)
    sprite('null', 4)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(-600000)
        AddY(-400000)
        Rotation(-30000)
        Size(2500)
    sprite('null', 32767)
    CreateObject('BurstDDEff_minicross', -1)
    ScreenShake(10000, 10000)

    def RunOnObject_1():
        AddX(-400000)
        AddY(100000)
        Rotation(-30000)
        Size(1800)
    label(1)
    sprite('null', 40)
    TriggerUponForState('BurstDDEff_minicross', 32)
    loopRest()


@State
def BurstDDEff_minicrossMato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 3)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(100000)
        AddY(100000)
        Rotation(10000)
        Size(800)
    sprite('null', 3)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(-80000)
        AddY(100000)
        Rotation(-10000)
        Size(1200)
    sprite('null', 3)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(125000)
        AddY(100000)
        Rotation(25000)
        Size(1600)
    sprite('null', 3)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(-125000)
        AddY(100000)
        Rotation(-25000)
        Size(800)
    sprite('null', 3)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(200000)
        AddY(100000)
        Rotation(30000)
        Size(1000)
    sprite('null', 32767)
    CreateObject('BurstDDEff_minicross', -1)

    def RunOnObject_1():
        AddX(-200000)
        AddY(100000)
        Rotation(-30000)
        Size(1500)
    label(1)
    sprite('null', 40)
    TriggerUponForState('BurstDDEff_minicross', 32)
    loopRest()


@State
def BurstDDEff_minicross():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('muef_440_sub')
        uponSendToLabel(32, 1)
        RemoveOnCallStateEnd(2)
    sprite('null', 15)
    SetScaleY(0)
    SetScaleSpeedY(14)
    sprite('null', 32767)
    SetScaleSpeedY(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    loopRest()


@State
def BurstDDEff_Circle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('muef_440hasira_circle', '')
        AddY(550000)
    sprite('null', 15)
    SetScaleSpeed(180)
    sprite('null', 45)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(45)


@State
def AssaultAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        AttackLevel_(3)
        Damage(800)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(2)
        AirUntechableTime(40)
        Stagger(37)
        Crumple(27)
        AirPushbackX(500)
        AirPushbackY(26000)
        PushbackX(9900)
        Hitstop(0)
        HitsparkSize(500)
        EnemyHitstopAddition(6, 6, 8)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackDirection(3)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            AttackOff()
            ObjectUpon(LANDING, 40)

        def upon_55():
            clearUponHandler(55)
            AttackOff()
            sendToLabel(1)

        def upon_PLAYER_DAMAGED():
            clearUponHandler(PLAYER_DAMAGED)
            AttackOff()
            ObjectUpon(LANDING, 40)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_YDistanceFromFloor <= 50000:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    AttackOff()
                    sendToLabel(1)
    sprite('null', 30)
    sprite('vr_bit_assault_atk', 10)
    sprite('vr_bit_assault_atk', 90)
    SetActionMark(1)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(60)


@State
def AssaultAtkOD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        AttackLevel_(3)
        Damage(800)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirUntechableTime(60)
        AirPushbackX(500)
        AirPushbackY(26000)
        PushbackX(1000)
        Hitstop(0)
        HitsparkSize(500)
        EnemyHitstopAddition(10, 10, 12)
        StarterRating(2)
        AttackDirection(3)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
            AttackOff()
            ObjectUpon(LANDING, 40)
            sendToLabel(100)

        def upon_55():
            clearUponHandler(55)
            AttackOff()
            sendToLabel(1)

        def upon_PLAYER_DAMAGED():
            clearUponHandler(PLAYER_DAMAGED)
            AttackOff()
            ObjectUpon(LANDING, 40)
        SetActionMark(0)

        def upon_EVERY_FRAME():
            if SLOT_YDistanceFromFloor <= 50000:
                if SLOT_2:
                    clearUponHandler(EVERY_FRAME)
                    AttackOff()
                    sendToLabel(1)
    sprite('null', 30)
    sprite('vr_bit_assault_atk', 10)
    sprite('vr_bit_assault_atk', 90)
    SetActionMark(1)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(60)
    ExitState()
    label(100)
    sprite('null', 100)
    CreateObject('AssaultAtkBomb', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(60)
    ExitState()


@State
def AssaultAtkBomb():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(700)
        if SLOT_137:
            DamageMultiplier(80)
        AirUntechableTime(40)
        Hitstop(6)
        Blockstun(7)
        AttackP2(94)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(500)
        AirPushbackY(26000)
        YImpulseBeforeWallbounce(1800)
        AttackDirection(3)
        UseFireHitspark(1)
        HitsparkSize(300)
        ReduceHitEffects(1)
        StarterRating(2)
        Visibility(1)
        DamageEffect(5, '')
    sprite('null', 10)
    sprite('vr_bit02_00', 3)
    CallPrivateEffect('muef_bitattack')
    Size(1500)
    CommonSE('016_explode_1')
    ScreenShake(10000, 10000)
    sprite('vr_bit02_00', 3)
    sprite('vr_bit02_00', 3)
    PerScale(115)
    sprite('vr_bit02_00', 5)
    PerScale(115)
    sprite('vr_bit02_00', 3)
    EndAttack()
    PerScale(87)
    sprite('vr_bit02_00', 3)
    PerScale(87)
    sprite('vr_bit02_00', 3)
    sprite('vr_bit02_00', 1)


@State
def ReflectionShotOD_Hontai():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(900)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirUntechableTime(25)
        AirPushbackX(1000)
        PushbackX(1000)
        Hitstop(0)
        EnemyHitstopAddition(6, 6, 8)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        AttackOff()
        CallPrivateFunction('ReflectionShotInit', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotODIdling', 0, 0, 0, 0, 0, 0,
                0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)

        def upon_LANDING():
            sendToLabel(580)
    sprite('null', 1)
    sprite('null', 1)
    CreateParticle('muef_401reflectionbit', -1)
    sprite('vr_bit00_00atk', 4)
    PrivateSE('muse_02')
    LinkParticle('muef_401reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(125)
    YAccel(125)
    Visibility(1)
    RefreshMultihit()
    sprite('vr_bit00_00atk', 4)
    XImpulseAcceleration(128)
    YAccel(128)
    sprite('vr_bit00_00atk', 2)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vr_bit00_00atk', 50)
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def ReflectionShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(900)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AirUntechableTime(25)
        AirPushbackX(1000)
        PushbackX(1000)
        Hitstop(0)
        EnemyHitstopAddition(6, 6, 8)
        UseSlashHitspark(1)
        AttackDirection(3)
        StarterRating(2)
        AttackOff()
        CallPrivateFunction('ReflectionShotInit', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('DriveLaserExInit', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_EVERY_FRAME():
            CallPrivateFunction('ReflectionShotODIdling', 0, 0, 0, 0, 0, 0,
                0, 0)

        def upon_48():
            CallPrivateFunction('DriveLaserExIdling', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_31():
            CallPrivateFunction('DriveLaserExDraw', 0, 0, 0, 0, 0, 0, 0, 0)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateObject('ReflectionShotHitEffect', 103)

        def upon_LANDING():
            sendToLabel(580)
    sprite('null', 10)
    sprite('null', 10)
    CreateParticle('muef_401reflectionbit', -1)
    sprite('vr_bit00_00atk', 4)
    PrivateSE('muse_02')
    LinkParticle('muef_401reflectionshot')
    Visibility(1)
    PopSpeedX()
    PopSpeedY()
    XImpulseAcceleration(125)
    YAccel(125)
    Visibility(1)
    RefreshMultihit()
    sprite('vr_bit00_00atk', 4)
    XImpulseAcceleration(128)
    YAccel(128)
    sprite('vr_bit00_00atk', 2)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vr_bit00_00atk', 50)
    loopRest()
    label(580)
    sprite('null', 20)
    physicsXImpulse(0)
    physicsYImpulse(0)
    ConstantAlphaModifier(-10)


@State
def Act2Event_Image():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ScreenPosition(1)
        XPositionRelativeFacing(-640000)
        AbsoluteY(0)
        Size(20000)
        uponSendToLabel(32, 0)
    sprite('vr_screen_black', 30)
    AlphaValue(0)
    ConstantAlphaModifier(4)
    sprite('vr_screen_black', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(120)
    label(0)
    sprite('vr_screen_black', 30)
    ConstantAlphaModifier(-4)
    sprite('vr_screen_black', 10)
    AlphaValue(0)
    ConstantAlphaModifier(0)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act3Event_Fade():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        SetZVal(-500)
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
def Eventoffset_Sosai():

    def upon_IMMEDIATE():
        XPositionRelativeFacingAbsolute(0)
        AbsoluteY(300000)
        DeviationX(-30000, 100000)
    sprite('null', 4)
    CreateParticle('ef_offset', 0)
    CommonSE('108_attack_offset')
    ScreenShake(30000, 30000)


@State
def Act3Event_Camera_muvstg():

    def upon_IMMEDIATE():
        CameraControlEnable(1)

        def upon_EVERY_FRAME():
            if SLOT_IsFacingRight:
                if SLOT_XDistanceFromCenterOfStage <= 0:
                    XPositionRelativeFacing(0)
                    EndMomentum(1)
                    CameraControlEnable(0)
                    sendToLabel(0)
                    clearUponHandler(EVERY_FRAME)
            elif SLOT_XDistanceFromCenterOfStage >= 0:
                XPositionRelativeFacing(0)
                EndMomentum(1)
                CameraControlEnable(0)
                sendToLabel(0)
                clearUponHandler(EVERY_FRAME)
    sprite('null', 600)
    AddInertia(20000)
    label(0)
    sprite('null', 5)


@State
def Act3Event_SwrodSwing_eff10():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        AlphaValue(255)
        BlendMode_Add()
    sprite('vrmuef404_07', 3)
    sprite('vrmuef404_08', 4)
    sprite('vrmuef404_09', 18)
    AbsoluteY(-64000)
    CreateObject('SwrodSwing_eff_tinkle2', 0)
    sprite('vrmuef404_10', 4)
    sprite('vrmuef404_11', 3)
    sprite('vrmuef404_12', 3)


@State
def Act3Event_SwrodSwing_eff_light2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        E0EAEffectDirection(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        PaletteIndex(3)
        BlendMode_Add()
    sprite('vrmuef404_07_', 3)
    sprite('vrmuef404_08_', 4)
    sprite('vrmuef404_09_', 18)
    AbsoluteY(-64000)
    sprite('vrmuef404_10_', 4)
    sprite('vrmuef404_11_', 3)
    sprite('vrmuef404_12_', 3)
