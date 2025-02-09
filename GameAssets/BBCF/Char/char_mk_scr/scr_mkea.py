@State
def EMB_MK():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        RenderLayer(5)
        Size(850)
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
def EMB_MK_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        RenderLayer(5)
        Size(850)
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
def EMB_MK_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_MK.DIG', 'ef_emb_MK_motion_000.mmot')
        RenderLayer(5)
        Size(850)
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

@State
def DriveRing():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)

        def upon_32():
            sendToLabel(22)

        def upon_33():
            AddX(-65000)
            AddY(200000)
            E0EAEffectPosition(3)

        def upon_34():
            AddX(-30000)
            AddY(240000)
            E0EAEffectPosition(3)

        def upon_35():
            AddX(-39000)
            AddY(325000)
            E0EAEffectPosition(3)

        def upon_58():
            if EnteredState('mk407_pos'):
                AddX(-158000)
                AddY(240000)
                E0EAEffectPosition(3)
            if EnteredState('Blockingpos'):
                AddX(-64000)
                AddY(245000)
                E0EAEffectPosition(3)
            if EnteredState('PowerDunkpos'):
                AddX(-72000)
                AddY(350000)
                E0EAEffectPosition(3)
            if EnteredState('PowerDunkStepBpos'):
                AddX(-68000)
                AddY(350000)
                E0EAEffectPosition(3)
            if EnteredState('PowerDunkStepCpos'):
                AddX(-70000)
                AddY(350000)
                E0EAEffectPosition(3)
            if EnteredState('UpperBodyBlowpos'):
                AddX(-115000)
                AddY(285000)
                E0EAEffectPosition(3)
            if EnteredState('DashStraightpos'):
                AddX(-78000)
                AddY(230000)
                E0EAEffectPosition(3)
            if EnteredState('BigPunchPos'):
                AddX(20000)
                AddY(308000)
                E0EAEffectPosition(3)
            if EnteredState('ShinSyouryu1Pos'):
                AddX(0)
                AddY(208000)
                E0EAEffectPosition(3)
            if EnteredState('ShinSyouryu2Pos'):
                AddX(-135000)
                AddY(270000)
                E0EAEffectPosition(3)
            if EnteredState('ShinSyouryu3Pos'):
                AddX(0)
                AddY(440000)
                E0EAEffectPosition(3)
            if EnteredState('AstralPos'):
                AddX(-195000)
                AddY(235000)
                E0EAEffectPosition(3)
        SLOT_51 = SLOT_103
        SLOT_51 = (SLOT_51 + 1)
        SLOT_104 = SLOT_51
        SLOT_104 = (SLOT_104 * 80)
        SLOT_105 = (-80)
        PaletteID(1)

        def upon_FRAME_STEP():
            if (SLOT_18 > SLOT_51):
                DeleteObject(23)
    sprite('null', 4)
    sprite('null', 117)
    CreateObject('DriveChargemc', -1)
    loopRest()
    label(22)
    sprite('null', 30)
    clearUponHandler(32)
    SetScaleSpeed(20)
    PassbackAddActionMarkToFunction('DriveChargemc', 33)
    E0EAEffectPosition(0)

@State
def FakeBunshinStepA():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        sendToLabelUpon(56, 99)
        WallCollisionDetection(1)
    sprite('mk404_00', 3)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('mk404_01', 2)
    physicsXImpulse(10000)
    sprite('mk404_02', 2)
    sprite('mk404_03', 4)
    XImpulseAcceleration(200)
    sprite('mk404_04', 4)
    XImpulseAcceleration(150)
    sprite('mk404_05', 4)
    sprite('mk404_06', 4)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    sprite('mk404_07', 4)
    sprite('mk404_08', 4)
    sprite('mk404_09', 4)
    label(99)
    sprite('keep', 4)
    XImpulseAcceleration(20)
    CreateParticle('mkef_fakebunshin', 0)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()

@State
def FakeBunshinStepB():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        sendToLabelUpon(56, 99)
        WallCollisionDetection(1)
    sprite('mk023_00', 2)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('mk023_01', 2)
    sprite('mk411_00', 4)
    physicsXImpulse(24000)
    physicsYImpulse(30000)
    setGravity(2000)
    sprite('mk411_01', 4)
    sprite('mk411_02', 3)
    sprite('mk411_03', 3)
    sprite('mk411_04', 1)
    sprite('mk411_04', 2)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    sprite('mk411_05', 3)
    sprite('mk411_12', 2)
    sprite('mk411_13', 2)
    sprite('mk411_14', 3)
    sprite('mk411_15', 2)
    sprite('mk411_16', 2)
    label(99)
    sprite('keep', 4)
    XImpulseAcceleration(20)
    CreateParticle('mkef_fakebunshin', 0)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()

@State
def FakeBunshinStepC():

    def upon_IMMEDIATE():
        NoDamageAction(1)
        sendToLabelUpon(56, 99)
        WallCollisionDetection(1)
    sprite('mk023_00', 2)
    EnableAfterimage(1)
    AfterimageBlendMode(0)
    sprite('mk023_01', 2)
    sprite('mk411_00', 4)
    physicsXImpulse(9000)
    physicsYImpulse(42000)
    setGravity(2200)
    sprite('mk411_01', 4)
    sprite('mk411_02', 3)
    sprite('mk411_03', 3)
    sprite('mk411_04', 1)
    sprite('mk411_04', 2)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    sprite('mk411_05', 3)
    sprite('mk411_12', 2)
    XImpulseAcceleration(80)
    sprite('mk411_13', 2)
    sprite('mk411_14', 3)
    sprite('mk411_15', 2)
    sprite('mk411_16', 2)
    label(99)
    sprite('keep', 4)
    XImpulseAcceleration(20)
    CreateParticle('mkef_fakebunshin', 0)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()

@State
def DonguriShot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(0)
        Damage(100)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(54, 1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        SLOT_6 = 1

        def upon_STATE_END():
            SLOT_6 = 0
    sprite('vr_donguri', 32767)
    AddRotationPerFrame(30000)
    AddY(450000)
    AddX(50000)
    setGravity(800)
    physicsYImpulse(20000)
    physicsXImpulse(4000)
    label(1)
    sprite('vr_donguri', 20)
    clearUponHandler(2)
    EndAttack()
    AddRotationPerFrame(-48000)
    YAccel(-40)
    XImpulseAcceleration(5)
    BlendMode_Normal()
    sprite('vr_donguri', 40)
    ConstantAlphaModifier(-30)

@State
def EnergyBall():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(350)
        SingleProration(1)
        Hitstop(0)
        EnemyHitstopAddition(3, 3, 4)
        AirPushbackX(2000)
        AirPushbackY(8000)
        PushbackX(2000)
        UseSlashHitspark(1)
        Unknown12052(1)
        StarterRating(2)
        HitsparkSize(400)
        AddX(160000)
        BlendMode_Add()
        CancelIfPlayerHit(3)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0

        def upon_ON_HIT_OR_BLOCK():
            AddActionMark(1)
            if (SLOT_2 == 3):
                clearUponHandler(10)
                HitsparkSize(1000)
                NoAttackDuringAction(1)

        def upon_OPPONENT_HIT():
            AttackDirection(4)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)

        def upon_41():
            NoAttackDuringAction(1)
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    Size(350)
    SetScaleSpeed(10)
    Visibility(1)
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(20)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(30)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(0)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test01', 3)
    RefreshMultihit()
    sprite('vr_shot_test01', 3)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 3)
    NoAttackDuringAction(1)
    CreateObject('mkef_EnergyBall', -1)
    sprite('vr_shot_test00', 28)
    CreateObject('mkef_EnergyBall_Koware', -1)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_shot_test01', 1)
    AttackLevel_(3)
    Damage(700)
    AttackP1(90)
    SingleProration(0)
    Hitstop(1)
    EnemyHitstopAddition(0, 12, 18)
    AirUntechableTime(25)
    AirPushbackX(20000)
    AirPushbackY(15000)
    ResetPushbackX()
    AttackDirection(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    BlendMode_Add()
    Visibility(1)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(0)
    sprite('vr_shot_test01', 5)
    CreateObject('mkef_EnergyBall_Punch', -1)
    NoAttackDuringAction(0)
    RefreshMultihit()
    physicsXImpulse(75000)
    SetAcceleration(-4000)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    XImpulseAcceleration(50)
    PerAcceleration(50)
    sprite('vr_shot_test01', 10)
    EndMomentum(1)
    loopRest()
    gotoLabel(101)
    label(1)
    sprite('vr_shot_test01', 1)
    AttackLevel_(4)
    Damage(800)
    AttackP1(90)
    SingleProration(0)
    Hitstop(1)
    EnemyHitstopAddition(0, 12, 18)
    AirUntechableTime(25)
    AirPushbackX(30000)
    AirPushbackY(15000)
    ResetPushbackX()
    AttackDirection(0)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    BlendMode_Add()
    Visibility(1)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(0)
    sprite('vr_shot_test01', 5)
    CreateObject('mkef_EnergyBall_Punch', -1)
    NoAttackDuringAction(0)
    RefreshMultihit()
    physicsXImpulse(85000)
    SetAcceleration(-4000)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    XImpulseAcceleration(50)
    PerAcceleration(50)
    sprite('vr_shot_test01', 10)
    EndMomentum(1)
    loopRest()
    gotoLabel(101)
    label(2)
    sprite('vr_shot_test01', 1)
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    SingleProration(0)
    Hitstop(1)
    EnemyHitstopAddition(0, 12, 18)
    AirUntechableTime(35)
    AirHitstunAnimation(19)
    AirPushbackX(50000)
    AirPushbackY(15000)
    ResetPushbackX()
    AttackDirection(0)
    FatalCounter(1)
    CHGroundedHitstunAnimation(12)
    CHAirHitstunAnimation(12)
    AirHitstunAfterWallbounce(50)
    CHWallbounceReboundTime(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    BlendMode_Add()
    Visibility(1)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(0)
    sprite('vr_shot_test01', 5)
    CreateObject('mkef_EnergyBall_Punch', -1)
    NoAttackDuringAction(0)
    RefreshMultihit()
    physicsXImpulse(95000)
    SetAcceleration(-4000)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    XImpulseAcceleration(50)
    PerAcceleration(50)
    sprite('vr_shot_test01', 10)
    EndMomentum(1)
    loopRest()
    gotoLabel(101)
    label(3)
    sprite('vr_shot_test01', 1)
    AttackLevel_(5)
    Damage(900)
    AttackP1(90)
    SingleProration(0)
    Hitstop(1)
    AirUntechableTime(35)
    EnemyHitstopAddition(0, 12, 18)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    ResetPushbackX()
    AttackDirection(0)
    FatalCounter(1)
    AirHitstunAfterWallbounce(50)
    CHWallbounceReboundTime(5)
    clearUponHandler(10)
    clearUponHandler(12)
    sendToLabelUpon(10, 100)
    BlendMode_Add()
    Visibility(1)
    CreateObject('mkef_EnergyBall', -1)
    SetScaleSpeed(0)
    sprite('vr_shot_test01', 5)
    CreateObject('mkef_EnergyBall_Punch', -1)
    NoAttackDuringAction(0)
    RefreshMultihit()
    physicsXImpulse(95000)
    SetAcceleration(-4000)
    sprite('vr_shot_test01', 10)
    SLOT_51 = 1
    XImpulseAcceleration(50)
    PerAcceleration(50)
    sprite('vr_shot_test01', 10)
    EndMomentum(1)
    loopRest()
    gotoLabel(101)
    label(100)
    if SLOT_51:
        _gotolabel(101)
    sprite('vr_shot_test01', 16)
    NoAttackDuringAction(1)
    XImpulseAcceleration(80)
    SetAcceleration(0)
    ExitState()
    label(101)
    sprite('vr_shot_test01', 10)
    NoAttackDuringAction(1)
    EndMomentum(1)
    SetAcceleration(0)
    SetScaleSpeed(-50)
    PassbackAddActionMarkToFunction('mkef_EnergyBall_Punch', 36)

@State
def ChargeRing():

    def upon_IMMEDIATE():
        LinkParticle('mkef_DriveChage_test')
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        RenderLayer(4)
        Size(1800)
        sendToLabelUpon(32, 22)
    sprite('null', 2)
    AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(20)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    AlphaValue(200)
    loopRest()
    label(22)
    sprite('null', 10)
    ConstantAlphaModifier(-25)

@State
def DriveChargemc():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Drivemc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectScale(2)
        RenderLayer(4)
        IgnoreScreenfreeze(1)
        sendToLabelUpon(44, 22)
        sendToLabelUpon(33, 22)
    sprite('null', 200)
    AlphaValue(255)
    loopRest()
    label(22)
    clearUponHandler(33)
    sprite('null', 8)
    AlphaValue(255)
    ConstantAlphaModifier(-40)
    sprite('null', 1)
    AlphaValue(0)

@State
def DriveChargeAura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        ColorForTransition(3355459839)
        RemoveOnCallStateEnd(3)
        sendToLabelUpon(32, 99)
        sendToLabelUpon(44, 99)
        ContinueState(160)
    sprite('vref_env', 15)
    SetScaleSpeed(200)
    sprite('vref_env', 200)
    SetScaleSpeed(0)
    label(99)
    sprite('vref_env', 10)
    clearUponHandler(32)
    clearUponHandler(44)
    RemoveOnCallStateEnd(0)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-40)

@State
def DriveChargeAuraAir():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        BlendMode_Add()
        Size(0)
        ColorForTransition(3355459839)
        sendToLabelUpon(32, 99)
        ContinueState(120)
    sprite('vref_env', 15)
    SetScaleSpeed(200)
    sprite('vref_env', 40)
    SetScaleSpeed(0)
    loopRest()
    label(99)
    sprite('vref_env', 14)
    E0EAEffectPosition(0)
    SetScaleSpeed(-100)
    ConstantAlphaModifier(-20)

@State
def DriveChargeWind():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_wind.DIG', 'mkef_wind_motion_000.mmot')
        FaceSpawnLocation()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        ColorForTransition(13172735)
        BlendMode_Add()
        Size(250)
        AddX(16000)
        AlphaValue(255)
        IgnoreScreenfreeze(1)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(36, 2)
    sprite('null', 5)
    ConstantAlphaModifier(20)
    SetScaleSpeed(20)
    sprite('null', 32767)
    SetScaleSpeed(0)
    loopRest()
    label(1)
    sprite('null', 5)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(200)
    ConstantAlphaModifier(-60)
    SetScaleXPerFrame(10)
    label(2)
    sprite('null', 15)
    E0EAEffectPosition(0)
    RemoveOnCallStateEnd(0)
    AlphaValue(200)
    ConstantAlphaModifier(-20)
    SetScaleXPerFrame(10)

@State
def DriveChargelightning():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        LinkParticle('mkef_lightorange')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        Size(800)
    sprite('null', 30)

@State
def Lightblue():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('mkef_lightblue')
    sprite('null', 24)

@State
def ShinigPunch_D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
    sprite('vrmkef203_00', 2)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    BlendMode_Add()
    sprite('vrmkef203_01', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef203_02', 2)
    ConstantAlphaModifier(-50)
    sprite('vrmkef203_02', 3)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)

@State
def ShinigPunchLvG_D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(2)
    sprite('vrmkef203_00', 2)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    BlendMode_Add()
    sprite('vrmkef203_01', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef203_02', 2)
    ConstantAlphaModifier(-50)
    sprite('vrmkef203_02', 3)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)

@State
def ShinigPunch_2D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
    sprite('vrmkef233_00', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    BlendMode_Add()
    sprite('vrmkef233_01', 2)
    ConstantAlphaModifier(-50)
    sprite('vrmkef233_01', 1)
    sprite('vrmkef233_01', 2)

@State
def ShinigPunchLvG_2D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(2)
    sprite('vrmkef233_00', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    BlendMode_Add()
    sprite('vrmkef233_01', 2)
    ConstantAlphaModifier(-50)
    sprite('vrmkef233_01', 1)
    sprite('vrmkef233_01', 2)

@State
def ShinigPunch_5D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
    sprite('vrmkef254_00', 2)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    BlendMode_Add()
    sprite('vrmkef254_01', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef254_02', 3)
    ConstantAlphaModifier(-50)
    sprite('vrmkef254_02', 3)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)

@State
def ShinigPunchLvG_5D():

    def upon_IMMEDIATE():
        RenderLayer(1)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(2)
    sprite('vrmkef254_00', 2)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    BlendMode_Add()
    sprite('vrmkef254_01', 5)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef254_02', 3)
    ConstantAlphaModifier(-50)
    sprite('vrmkef254_02', 3)
    CreateObject('Lightblue', 0)
    CreateObject('Lightblue', 1)

@State
def DriveLv1PunchefD():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv1Punchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv2PunchefD():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Punchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddX(-15000)
    sprite('null', 5)
    AddX(20000)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv3PunchefD():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        sendToLabelUpon(33, 1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-8)
    ExitState()
    label(1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 12)
    ConstantAlphaModifier(-12)

@State
def DriveLvG_PunchefD():

    def upon_IMMEDIATE():
        LinkParticle('mkef_LvGPunchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLvG_PunchefD():

    def upon_IMMEDIATE():
        LinkParticle('mkef_LvGPunchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLv1Punchef2D():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv1Punchmc')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        RotationAngle(270000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv2Punchef2D():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Punchmc')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        RotationAngle(270000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv3Punchef2D():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        RotationAngle(270000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLvG_Punchef2D():

    def upon_IMMEDIATE():
        LinkParticle('mkef_LvGPunchmc')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        RotationAngle(270000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLv1PunchefPowerDunk():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv1Punchmc')
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(80000)
        sendToLabelUpon(32, 70)
    sprite('null', 5)
    E0EAEffectPosition(3)
    sprite('null', 3)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)
    label(70)
    sprite('null', 8)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-30)

@State
def DriveLv2PunchefPowerDunk():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Punchmc')
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(80000)
    sprite('null', 5)
    E0EAEffectPosition(3)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-10)

@State
def DriveLv3PunchefPowerDunk():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(80000)
    sprite('null', 8)
    E0EAEffectPosition(3)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-8)

@State
def DriveLvG_PunchefPowerDunk():

    def upon_IMMEDIATE():
        LinkParticle('mkef_LvGPunchmc')
        BlendMode_Add()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(80000)
    sprite('null', 8)
    E0EAEffectPosition(3)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-8)

@State
def DriveLv1PunchefSyouryu2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv1Punchmc')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RotationAngle(290000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv2PunchefSyouryu2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Punchmc')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RotationAngle(290000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def DriveLv3PunchefSyouryu2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RotationAngle(290000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLv3PunchefSyouryu():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RotationAngle(270000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def DriveLv3PunchefSyouryu_Air():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        RotationAngle(270000)
    sprite('null', 4)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def mkef_hit_low():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('mkef_hit_low', -1)

@State
def mkef_hit_middle():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('mkef_hit_middle', -1)

@State
def mkef_hit_high():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('mkef_hit_high', -1)

@State
def mkef_hit_tailsp():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('mkef_hit_tailsp', -1)
    PrivateSE('mkse_06')
    PrivateSE('mkse_06')

@State
def mkef_hit_tailsp_nage():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('mkef_hit_tailsp_nage', -1)
    PrivateSE('mkse_06')

@State
def mkef_hibana():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        LinkParticle('mkef_hibana')
    sprite('null', 6)

@State
def mkef_EnergyBall():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        LinkParticle('mkef_EnergyBall')
        Size(750)
    sprite('null', 6)

@State
def mkef_EnergyBall_Punch():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        LinkParticle('mkef_400energyball')
        AlphaValue(255)
        sendToLabelUpon(54, 11)
        sendToLabelUpon(36, 11)
    sprite('null', 30)
    sprite('null', 1)
    Unknown23090(23)
    loopRest()
    ExitState()
    label(11)
    sprite('null', 4)
    sprite('null', 5)
    ConstantAlphaModifier(-50)
    sprite('null', 1)
    AlphaValue(0)
    loopRest()
    ExitState()

@State
def mkef_EnergyBall_Koware():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        LinkParticle('mkef_400energyball')
        Size(600)
        BlendMode_Add()
    sprite('null', 8)
    EndSE()
    ConstantAlphaModifier(-30)
    SetScaleSpeed(10)
    sprite('null', 1)
    AlphaValue(0)

@State
def SyouryuUpper():

    def upon_IMMEDIATE():
        LinkParticle('mkef_401upperpunch')
        E0EAEffectPosition(3)
    sprite('null', 8)
    RotationAngle(15000)
    sprite('null', 32)

@State
def PowerDunkAirwallLv2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Puncheairwall')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 75)
    RotationAngle(80000)

@State
def PowerDunkAirwallLv3():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Puncheairwall')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 75)
    RotationAngle(80000)

@State
def PowerDunkAirwallLvG():

    def upon_IMMEDIATE():
        LinkParticle('mkef_PuncheairwallLvG')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 75)
    RotationAngle(80000)

@State
def BlockingPunchLv1():

    def upon_IMMEDIATE():
        LinkParticle('mkef_403Lv1punch')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
    sprite('null', 5)
    AddY(6000)
    sprite('null', 65)
    AddX(75000)

@State
def BlockingPunchLv2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_403Lv2punch')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
        E0EAEffectPosition(3)
    sprite('null', 5)
    AddY(6000)
    sprite('null', 65)
    AddX(75000)

@State
def BlockingPunchLv3():

    def upon_IMMEDIATE():
        LinkParticle('mkef_403Lv3punch')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 70)
    E0EAEffectPosition(3)
    AddY(6000)
    AddX(40000)

@State
def BlockingPunchLv3_G():

    def upon_IMMEDIATE():
        LinkParticle('mkef_403Lv3punch_G')
        RemoveOnCallStateEnd(3)
        IgnorePauses(3)
    sprite('null', 70)
    E0EAEffectPosition(3)
    AddY(6000)
    AddX(40000)

@State
def BlockingSpeedLine():

    def upon_IMMEDIATE():
        LinkParticle('mkef_403speedline00')
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(3)
    sprite('null', 12)
    AbsoluteY(200000)
    AddX(-80000)

@State
def BlockingWind():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_screw.DIG', 'mkef_screw_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        BlendMode_Add()
        SetScaleY(500)
        SetScaleX(750)
        AlphaValue(200)
    sprite('null', 3)
    ConstantAlphaModifier(-15)
    AddX(-300000)
    AddY(-30000)
    physicsXImpulse(-10000)
    sprite('null', 21)
    physicsXImpulse(-10000)

@State
def EntryMant():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('vrmkef600m_00', 6)
    AddY(10000)
    sprite('vrmkef600m_01', 3)
    AddY(180000)
    sprite('vrmkef600m_01', 3)
    AddY(100000)

@State
def GuardCrash():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmkef414_00', 4)
    CreateObject('mkef_414Lv3airwall', 0)
    sprite('vrmkef414_01', 4)
    sprite('vrmkef414_02', 4)
    sprite('vrmkef414_03', 4)

@State
def mkef_414Lv3airwall():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_414')
    sprite('null', 30)
    RotationAngle(90000)

@State
def mkef413_lv1():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmkef413_00', 1)
    CreateObject('DriveLv1PunchefD413', 0)
    Visibility(1)

@State
def DriveLv1PunchefD413():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('mkef_Lv1Punchmc')
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def mkef413_lv2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmkef413_00', 1)
    CreateObject('DriveLv2PunchefD413', 0)
    Visibility(1)

@State
def DriveLv2PunchefD413():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('mkef_Lv2Punchmc')
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    AddX(20000)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def mkef413_lv3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrmkef413_00', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    CreateObject('DriveLv3PunchefD413', 0)
    sprite('vrmkef413_01', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef413_02', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    ConstantAlphaModifier(-50)

@State
def DriveLv3PunchefD413():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_Lv3Punchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def mkef413_lvG():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(2)
        BlendMode_Add()
    sprite('vrmkef413_00', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    CreateObject('DriveLvG_PunchefD413', 0)
    sprite('vrmkef413_01', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    AlphaValue(200)
    sprite('vrmkef413_02', 2)
    CreateObject('Lightblue', 1)
    CreateObject('Lightblue', 2)
    ConstantAlphaModifier(-50)

@State
def DriveLvG_PunchefD413():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_LvGPunchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    E0EAEffectPosition(0)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def Drive412Lv1():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv1Punchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(-60000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def Drive412Lv2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv2Punchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(-60000)
    sprite('null', 5)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-10)

@State
def Drive412Lv3():

    def upon_IMMEDIATE():
        LinkParticle('mkef_Lv3Punchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(-60000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def Drive412LvG():

    def upon_IMMEDIATE():
        LinkParticle('mkef_LvGPunchmc')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RotationAngle(-60000)
    sprite('null', 8)
    sprite('null', 3)
    ConstantAlphaModifier(-25)
    sprite('null', 19)
    ConstantAlphaModifier(-8)

@State
def Drive412Lv1_hit():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_412Lv1')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 60)
    RotationAngle(32000)

@State
def Drive412Lv2_hit():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_412Lv2')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 60)
    RotationAngle(32000)

@State
def Drive412Lv3_hit():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_412Lv3')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 60)
    RotationAngle(32000)

@State
def Drive412LvG_hit():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('mkef_412LvG')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 60)
    RotationAngle(32000)

@State
def mkef_415_punch():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        BlendMode_Add()
        Eff3DEffect('mkef_415', '')
        FaceSpawnLocation()
        Size(1250)
    sprite('null', 16)
    CreateParticle('mkef_415', -1)
    ConstantAlphaModifier(-16)

@State
def mkef_415_atk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        StrikeProjectileLevel(1)
        ProjectileLevel(0)
        MoveAttributes(0, 1, 0, 0, 0)
        Damage(500)
        Hitstop(12)
        Hitstun(20)
        CHHitstun(20)
        AirUntechableTime(22)
        AttackP1(80)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(1)
        AirPushbackX(30000)
        AirPushbackY(11666)
        PushbackX(50000)
        StarterRating(2)
        Unknown11109(1)
        AutoHitStopSending(1)
        PassByArmor(1)

        def upon_32():
            NoAttackDuringAction(1)

        def upon_FRAME_STEP():
            CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
            if (SLOT_51 == 0):
                DoNotHitKnockedDownOpp(1)
            else:
                DoNotHitKnockedDownOpp(0)

        def upon_ON_HIT_OR_BLOCK():
            PassbackAddActionMarkToFunction('SiriusJolt', 32)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(3)
        IgnorePauses(3)
    sprite('mk415_10_dmyAtk', 3)

@State
def BigPunch_SE():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(0)
        IgnorePauses(3)
        ContinueState(50)
    label(0)
    sprite('null', 4)
    CommonSE('019_quake_0')
    ScreenShake(1000, 0)
    loopRest()
    gotoLabel(0)

@State
def mk430cutin_up():

    def upon_IMMEDIATE():
        RenderLayer(2)
        IgnorePauses(3)
        PaletteIndex(0)
        BlendMode_Normal()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-580000)
        XPositionRelativeFacingAbsolute(640000)
    sprite('mk430cutin_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    sprite('mk430cutin_01', 5)
    sprite('mk430cutin_00', 7)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 7)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 7)
    sprite('mk430cutin_01', 7)
    sprite('mk430cutin_00', 5)
    ConstantAlphaModifier(-25)
    sprite('mk430cutin_01', 5)

@State
def mkef_430circlering_lv1():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430circlering')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1000)
        AddY(20000)
    sprite('null', 45)
    sprite('null', 30)
    ConstantAlphaModifier(-20)

@State
def mkef_430circlering_lv2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430circlering')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1110)
        AddY(20000)
    sprite('null', 45)
    sprite('null', 30)
    ConstantAlphaModifier(-20)

@State
def mkef_430circlering_lv3():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430circlering')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1220)
        AddY(20000)
    sprite('null', 50)
    sprite('null', 35)
    ConstantAlphaModifier(-20)

@State
def mkef_430bigpunch_lv2():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430bigpunch04')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1000)
        AddX(800000)
    sprite('null', 30)
    sprite('null', 40)
    ConstantAlphaModifier(-20)

@State
def mkef_430bigpunch_lv3():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430bigpunch')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1220)
        AddX(800000)
    sprite('null', 30)
    sprite('null', 40)
    ConstantAlphaModifier(-20)

@State
def mkef_430bigpunch_lvG():

    def upon_IMMEDIATE():
        LinkParticle('mkef_430bigpunch')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(2020)
        AddX(800000)
    sprite('null', 30)
    sprite('null', 40)
    ConstantAlphaModifier(-20)

@State
def mk430cutin_lv1():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        AttackP2(79)
        MinimumDamage(25)
        AirUntechableTime(100)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        EnemyHitstopAddition(0, 20, 20)
        UsePunchHitspark(1)
        StarterRating(2)
        RenderLayer(15)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(820)
        AddX(-15000)
        AddY(-5000)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('null', 1)
    CreateObject('mk430effLv1', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    AddX(30000)
    sprite('mk430_punch01', 1)
    AddX(35000)
    sprite('mk430_punchlv01', 4)
    physicsXImpulse(0)
    AddX(25000)
    sprite('mk430_punchlv01', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv01', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv01', 15)
    StartMultihit()
    ConstantAlphaModifier(-25)
    BlendMode_Add()

@State
def mk430effLv1():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        SetScaleX(1400)
        SetScaleY(1600)
        AddX(200000)
        AlphaValue(0)
        BlendMode_Add()
        RenderLayer(15)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('vrmkef430add_00ex00', 4)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(30)
    sprite('vrmkef430add_00', 23)
    AlphaValue(160)
    ConstantAlphaModifier(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lv2():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(82)
        MinimumDamage(25)
        AirUntechableTime(100)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        EnemyHitstopAddition(0, 20, 20)
        UsePunchHitspark(1)
        StarterRating(2)
        RenderLayer(15)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(980)
        AddX(-160000)
        AddY(400000)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('null', 1)
    CreateObject('mkef_430bigpunch_lv2', -1)
    CreateObject('mk430effLv2', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    AddX(30000)
    sprite('mk430_punch01', 1)
    AddX(35000)
    sprite('mk430_punchlv02', 4)
    physicsXImpulse(0)
    AddX(35000)
    sprite('mk430_punchlv02', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv02', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv02', 15)
    StartMultihit()
    ConstantAlphaModifier(-25)
    BlendMode_Add()

@State
def mk430effLv2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        SetScaleX(1700)
        SetScaleY(2000)
        AddX(220000)
        AlphaValue(0)
        BlendMode_Add()
        RenderLayer(15)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('vrmkef430add_00ex00', 5)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(30)
    sprite('vrmkef430add_00', 22)
    AlphaValue(180)
    ConstantAlphaModifier(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lv3():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(2600)
        AttackP1(80)
        AttackP2(84)
        MinimumDamage(25)
        AirUntechableTime(100)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        EnemyHitstopAddition(0, 20, 20)
        UsePunchHitspark(1)
        FatalCounter(1)
        StarterRating(2)
        RenderLayer(15)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1000)
        AddX(45000)
        AddY(405000)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('null', 1)
    CreateObject('mkef_430bigpunch_lv3', -1)
    CreateObject('mk430effLv3', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    AddX(30000)
    sprite('mk430_punch01', 1)
    AddX(35000)
    sprite('mk430_punchlv03', 1)
    AddX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    AddX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    ConstantAlphaModifier(-15)
    BlendMode_Add()

@State
def mk430effLv3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(2020)
        AddX(100000)
        AlphaValue(0)
        BlendMode_Add()
        RenderLayer(15)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('vrmkef430add_00ex00', 5)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(30)
    sprite('vrmkef430add_00', 22)
    AlphaValue(200)
    ConstantAlphaModifier(0)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk430cutin_lvG():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(3000)
        AttackP1(80)
        AttackP2(84)
        MinimumDamage(25)
        AirUntechableTime(100)
        GroundedHitstunAnimation(17)
        AirHitstunAnimation(17)
        AirPushbackX(50000)
        PushbackX(36000)
        Hitstop(0)
        EnemyHitstopAddition(0, 20, 20)
        UsePunchHitspark(1)
        FatalCounter(1)
        StarterRating(2)
        RenderLayer(15)
        PaletteIndex(2)
        BlendMode_Normal()
        Size(1000)
        AddX(45000)
        AddY(405000)
        BlendMode_Add()
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('null', 1)
    CreateObject('mkef_430bigpunch_lvG', -1)
    CreateObject('mk430effLvG', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    AddX(30000)
    sprite('mk430_punch01', 1)
    AddX(35000)
    sprite('mk430_punchlv03', 1)
    AddX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    AddX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    ConstantAlphaModifier(-15)

@State
def mk430effLvG():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        Size(2020)
        AddX(100000)
        AlphaValue(0)
        BlendMode_Add()
        RenderLayer(15)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('vrmkef430add_00ex00', 5)
    E0EAEffectPosition(2)
    ConstantAlphaModifier(30)
    sprite('vrmkef430add_00', 22)
    ConstantAlphaModifier(0)
    AlphaValue(150)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mkef_circle_small():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(640)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 25)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-15)

@State
def mkef_circle_middle():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(720)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 25)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-15)

@State
def mkef_circle_large():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_circle.DIG', 'mkef_circle_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(820)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 25)
    AlphaValue(255)
    sprite('null', 20)
    ConstantAlphaModifier(-15)

@State
def mkef_mahojin_small():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(660)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 30)
    AlphaValue(255)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    sprite('null', 60)

@State
def mkef_mahojin_middle():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(760)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 35)
    AlphaValue(255)
    sprite('null', 35)
    ConstantAlphaModifier(-10)
    sprite('null', 60)

@State
def mkef_mahojin_large():

    def upon_IMMEDIATE():
        Eff3DEffect('mkef_mahojin.DIG', 'mkef_mahojin_motion_000.mmot')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        BlendMode_Add()
        Size(840)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 38)
    AlphaValue(255)
    sprite('null', 38)
    ConstantAlphaModifier(-10)
    sprite('null', 60)

@State
def mk431cutin_up():

    def upon_IMMEDIATE():
        PaletteIndex(0)
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        SetPosXByScreenPer(50)
        AbsoluteY(1825000)
        sendToLabelUpon(32, 23)
    sprite('mk431cutin_00', 5)
    Size(1000)
    AlphaValue(0)
    ConstantAlphaModifier(25)
    sprite('mk431cutin_01', 5)
    sprite('mk431cutin_00', 7)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 7)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 7)
    sprite('mk431cutin_01', 7)
    sprite('mk431cutin_00', 5)
    ConstantAlphaModifier(-25)
    sprite('mk431cutin_01', 5)
    sprite('mk431cutin_01', 1)
    AlphaValue(0)
    loopRest()
    label(23)
    sprite('mk431cutin_00', 5)
    ConstantAlphaModifier(-50)
    sprite('mk431cutin_01', 1)
    AlphaValue(0)

@State
def mk431cutin_punchLv1():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddY(595000)
        RotationAngle(10000)
        Size(750)
    sprite('mk431cutin_02', 6)
    CreateObject('mk431effLv1', -1)
    AlphaValue(0)
    ConstantAlphaModifier(35)
    sprite('mk431cutin_02', 37)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-40000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    ConstantAlphaModifier(-35)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    AlphaValue(0)

@State
def mk431effLv1():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(1800)
        RotationAngle(90000)
        AlphaValue(128)
        BlendMode_Add()
    sprite('vrmkef430add_00', 45)
    AddY(-30000)
    E0EAEffectPosition(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLv2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddY(595000)
        Size(850)
        RotationAngle(10000)
    sprite('mk431cutin_02', 6)
    CreateObject('mk431effLv2', -1)
    AlphaValue(0)
    ConstantAlphaModifier(35)
    sprite('mk431cutin_02', 35)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    ConstantAlphaModifier(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    AlphaValue(0)

@State
def mk431effLv2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(2000)
        RotationAngle(90000)
        AlphaValue(200)
        BlendMode_Add()
    sprite('vrmkef430add_00', 45)
    E0EAEffectPosition(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLv3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        PaletteIndex(1)
        BlendMode_Normal()
        AddY(640000)
        Size(950)
        RotationAngle(10000)
    sprite('mk431cutin_02', 6)
    CreateObject('mk431effLv3', -1)
    AlphaValue(0)
    ConstantAlphaModifier(35)
    sprite('mk431cutin_02', 35)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    ConstantAlphaModifier(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    AlphaValue(0)

@State
def mk431effLv3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(2200)
        RotationAngle(90000)
        AlphaValue(200)
        BlendMode_Add()
    sprite('vrmkef430add_00', 45)
    E0EAEffectPosition(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431cutin_punchLvG():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(2)
        PaletteIndex(2)
        BlendMode_Normal()
        AddY(640000)
        Size(950)
        RotationAngle(10000)
    sprite('mk431cutin_02', 6)
    CreateObject('mk431effLvG', -1)
    AlphaValue(0)
    ConstantAlphaModifier(35)
    sprite('mk431cutin_02', 35)
    ConstantAlphaModifier(0)
    AlphaValue(255)
    sprite('mk431cutin_02', 3)
    physicsYImpulse(-60000)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    ConstantAlphaModifier(-30)
    sprite('mk431cutin_02', 3)
    YAccel(50)
    sprite('mk431cutin_02', 21)
    sprite('mk431cutin_02', 1)
    AlphaValue(0)

@State
def mk431effLvG():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(2)
        Size(2200)
        RotationAngle(90000)
        AlphaValue(150)
        BlendMode_Add()
    sprite('vrmkef430add_00', 45)
    E0EAEffectPosition(2)
    sprite('vrmkef430add_01', 4)
    sprite('vrmkef430add_02', 4)
    sprite('vrmkef430add_03', 4)
    sprite('vrmkef430add_04', 4)
    E0EAEffectPosition(0)
    ConstantAlphaModifier(-15)
    sprite('vrmkef430add_05', 4)
    sprite('vrmkef430add_06', 4)

@State
def mk431dummy():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('mk431_18', 20)

@State
def mkef_431Lv1first():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv1first')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1000)
    sprite('null', 80)
    RotationAngle(27000)

@State
def mkef_431Lv2first():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv2first')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1100)
    sprite('null', 80)
    RotationAngle(27000)

@State
def mkef_431Lv3first():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv3first')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 80)
    RotationAngle(27000)

@State
def mkef_431Lv1secondtame():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv1secondtame')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(900)
    sprite('null', 80)

@State
def mkef_431Lv2secondtame():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv2secondtame')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1100)
    sprite('null', 80)

@State
def mkef_431Lv3secondtame():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv3secondtame')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 80)

@State
def mkef_431_2ndsub_back():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431_2nd000_back')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1100)
    sprite('null', 80)

@State
def mkef_431Lv1second():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv1second')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1200)
    sprite('null', 80)

@State
def mkef_431Lv2second():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv2second')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 80)

@State
def mkef_431Lv3second():

    def upon_IMMEDIATE():
        LinkParticle('mkef_431Lv3second')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(1800)
    sprite('null', 80)

@State
def mkef_jumpsmoke11():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke02')
        IgnoreScreenfreeze(1)
        Size(800)
    sprite('null', 40)

@State
def mkef_jumpsmoke12():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke02')
        IgnoreScreenfreeze(1)
        Size(1100)
    sprite('null', 40)

@State
def mkef_jumpsmoke13():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke02')
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 40)

@State
def mkef_jumpsmoke21():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke')
        IgnoreScreenfreeze(1)
        Size(800)
    sprite('null', 40)

@State
def mkef_jumpsmoke22():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke')
        IgnoreScreenfreeze(1)
        Size(1100)
    sprite('null', 40)

@State
def mkef_jumpsmoke23():

    def upon_IMMEDIATE():
        LinkParticle('mkef_jumpsmoke')
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 40)

@State
def mk450_energy():

    def upon_IMMEDIATE():
        LinkParticle('mk450_energy')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(700)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 30)
    AlphaValue(255)
    sprite('null', 30)
    ConstantAlphaModifier(-10)
    sprite('null', 60)

@State
def mk450_tame():

    def upon_IMMEDIATE():
        LinkParticle('mk450_tame2')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(600)
        AlphaValue(0)
        sendToLabelUpon(32, 80)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 115)
    AlphaValue(255)
    label(80)
    sprite('null', 10)
    ConstantAlphaModifier(-25)
    sprite('null', 1)
    AlphaValue(0)

@State
def mk450_syogeki():

    def upon_IMMEDIATE():
        LinkParticle('mk450_syogeki')
        BlendMode_Add()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        Size(1400)
    sprite('null', 12)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)

@State
def mk450_impact():

    def upon_IMMEDIATE():
        LinkParticle('mk450_impact')
        BlendMode_Add()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        Size(800)
        AlphaValue(0)
        sendToLabelUpon(32, 81)
    sprite('null', 5)
    ConstantAlphaModifier(50)
    sprite('null', 115)
    AlphaValue(255)
    label(81)
    sprite('null', 10)
    ConstantAlphaModifier(-35)
    sprite('null', 1)
    AlphaValue(0)

@State
def mk450_bunsan():

    def upon_IMMEDIATE():
        LinkParticle('mk450_bunsan')
        BlendMode_Add()
        E0EAEffectPosition(3)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(3)
        Size(1000)
    sprite('null', 60)

@State
def mk450_footef():

    def upon_IMMEDIATE():
        LinkParticle('mk450_footef')
        BlendMode_Add()
        Size(1000)
    sprite('null', 27)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)

@State
def mk450_bgef():

    def upon_IMMEDIATE():
        LinkParticle('mkef_450bg')
        BlendMode_Add()
        AlphaValue(0)
        AddY(-50000)
    sprite('null', 9)
    ConstantAlphaModifier(25)
    sprite('null', 174)
    AlphaValue(255)

@State
def mk450_hibana():

    def upon_IMMEDIATE():
        LinkParticle('mkef_450hibana')
        BlendMode_Add()
    sprite('null', 164)

@State
def mk450cutin_tame():

    def upon_IMMEDIATE():
        RenderLayer(2)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        PaletteIndex(0)
        BlendMode_Add()
        AddY(290000)
    sprite('mk450cutin_00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('mk450cutin_01', 6)
    AlphaValue(255)
    sprite('mk450cutin_02', 7)
    sprite('mk450cutin_03', 6)
    sprite('mk450cutin_03', 6)
    ConstantAlphaModifier(-35)

@State
def mk450cutin_impact():

    def upon_IMMEDIATE():
        RenderLayer(1)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Normal()
        AddY(245000)
    sprite('mk450cutin_04', 4)
    CreateObject('mk450_impactline', 0)
    sprite('mk450cutin_05', 4)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    CreateObject('mk450_kirari', 0)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)
    sprite('mk450cutin_04', 6)
    sprite('mk450cutin_05', 6)

@State
def mk450cutin_impact_small():

    def upon_IMMEDIATE():
        RenderLayer(4)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        PaletteIndex(0)
        BlendMode_Normal()
        AddX(-390000)
        AddY(-89500)
    sprite('mk450cutin_06', 4)
    sprite('mk450cutin_07', 4)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)
    sprite('mk450cutin_06', 6)
    sprite('mk450cutin_07', 6)

@State
def mk450_impactline():

    def upon_IMMEDIATE():
        LinkParticle('mk450_impactline')
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Size(500)
    sprite('null', 80)
    AlphaValue(255)
    sprite('null', 10)
    ConstantAlphaModifier(-30)
    sprite('null', 1)
    AlphaValue(0)

@State
def mk450_kirari():

    def upon_IMMEDIATE():
        LinkParticle('mk450_kirari')
        BlendMode_Add()
        Size(750)
    sprite('null', 50)

@State
def AstWhite():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        RenderLayer(4)
        E0EAEffectPosition(3)
        AbsoluteY(340000)
        Size(10000)
        BlendMode_Add()
        AlphaValue(0)
    sprite('vr_white', 8)
    ConstantAlphaModifier(30)
    sprite('vr_white', 15)
    sprite('vr_white', 8)
    AlphaValue(240)
    ConstantAlphaModifier(-30)

@State
def mk450_kamifubuki():

    def upon_IMMEDIATE():
        LinkParticle('mk450_kamifubuki')
        BlendMode_Normal()
    sprite('null', 600)

@State
def AstralHeatKillObject():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        Damage(5000)
        MinimumDamage(100)
        AttackDirection(3)
        FinishBG(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(10000)
        HitAnywhere(1)
        TeleportToObject(22)
        Visibility(1)
        Size(3000)
    sprite('vr_donguri', 1)
    TeleportToObject(22)
    sprite('vr_donguri', 1)
    TeleportToObject(22)
    sprite('vr_donguri', 1)
    TeleportToObject(22)
    sprite('vr_donguri', 1)
    TeleportToObject(22)

@State
def RLAstLockmc():

    def upon_IMMEDIATE():
        Visibility(1)
        ParticleLayer(5)
        CallPrivateEffect('rlef_ashlock_mc')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)

@State
def RLAstLockAura():

    def upon_IMMEDIATE():
        Visibility(1)
        CallPrivateEffect('rlef_ashlock_aura')
        RemoveOnCallStateEnd(3)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        E0EAEffectPosition(22)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)

        def upon_56():
            CameraControlEnable(0)
            CameraFast(0)
            CameraNoScreenCollision(0)
    sprite('null', 25)
    sprite('null', 300)
    E0EAEffectPosition(0)
    ExitState()
    label(0)
    sprite('null', 15)
    CameraFast(1)
    physicsYImpulse(100000)
    sprite('null', 300)
    EndMomentum(1)
    ExitState()
    label(1)
    sprite('null', 5)
    sprite('null', 15)
    physicsYImpulse(-100000)
    sprite('null', 300)
    EndMomentum(1)
    ExitState()
    label(2)
    sprite('null', 10)
    physicsXImpulse(-70000)
    sprite('null', 300)
    EndMomentum(1)
    ExitState()
    label(3)
    sprite('null', 5)
    physicsXImpulse(100000)
    CameraControlEnable(0)
    sprite('null', 1)
    EndMomentum(1)
    CameraNoScreenCollision(0)
    ExitState()
    label(4)
    sprite('null', 5)
    physicsXImpulse(100000)
    CameraControlEnable(0)
    sprite('null', 1)
    EndMomentum(1)
    CameraNoScreenCollision(0)

@State
def mk440cutin():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(1)
        IgnorePauses(3)
        E0EAEffectPosition(3)
        AddX(-100000)
        AddY(100000)
        Size(1600)
    sprite('null', 11)
    CreateObject('mk440cutinEffStart', -1)
    sprite('mk440cutin_00', 3)
    CreateObject('mk440cutinEff', -1)
    sprite('mk440cutin_01', 3)
    sprite('mk440cutin_02', 3)
    physicsXImpulse(30000)
    SetAcceleration(10000)
    physicsYImpulse(-8000)
    setGravity(-2000)
    ConstantAlphaModifier(-24)
    sprite('mk440cutin_03', 1)
    SetAcceleration(0)
    sprite('mk440cutin_04', 5)
    XImpulseAcceleration(3)

@State
def mk440cutinEffStart():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrmkeff440_00', 2)
    sprite('vrmkeff440_01', 3)
    sprite('vrmkeff440_02', 3)
    sprite('vrmkeff440_03', 3)

@State
def mk440cutinEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrmkeff440_04', 3)
    sprite('vrmkeff440_05', 3)
    sprite('vrmkeff440_06', 3)
    sprite('vrmkeff440_07', 1)
    sprite('vrmkeff440_08', 3)
    sprite('null', 3)
    CreateObject('mk440cutinEffEnd', -1)

@State
def mk440cutinEffEnd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        Size(1600)
    sprite('vrmkeff440_09', 4)
    sprite('vrmkeff440_10', 4)
    sprite('vrmkeff440_11', 4)
    ConstantAlphaModifier(-23)
    sprite('vrmkeff440_12', 4)
    sprite('vrmkeff440_13', 4)

@State
def mk440cutin_Active():

    def upon_IMMEDIATE():
        RenderLayer(1)
        PaletteIndex(2)
        E0EAEffectPosition(3)
        AddX(-100000)
        AddY(100000)
        Size(1800)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('null', 11)
    CreateObject('mk440cutinEffStarEx', -1)
    sprite('mk440cutin_00', 3)
    CreateObject('mk440cutinEffEx', -1)
    IgnorePauses(3)
    sprite('mk440cutin_01', 3)
    sprite('mk440cutin_02', 3)
    ConstantAlphaModifier(-24)
    physicsXImpulse(30000)
    SetAcceleration(10000)
    physicsYImpulse(-8000)
    setGravity(-2000)
    sprite('mk440cutin_03', 1)
    physicsYImpulse(15000)
    SetAcceleration(0)
    sprite('mk440cutin_04', 5)
    XImpulseAcceleration(3)

@State
def mk440cutinEffStarEx():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrmkeff440_00', 2)
    sprite('vrmkeff440_01', 3)
    sprite('vrmkeff440_02', 3)
    sprite('vrmkeff440_03', 3)

@State
def mk440cutinEffEx():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrmkeff440_04', 3)
    sprite('vrmkeff440_05', 3)
    sprite('vrmkeff440_06', 3)
    sprite('vrmkeff440_07', 1)
    sprite('vrmkeff440_08', 3)
    sprite('null', 3)
    CreateObject('mk440cutinEffEndEX', -1)

@State
def mk440cutinEffEndEX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        Size(1800)
    sprite('vrmkeff440_09', 4)
    sprite('vrmkeff440_10', 4)
    sprite('vrmkeff440_11', 4)
    ConstantAlphaModifier(-23)
    sprite('vrmkeff440_12', 4)
    sprite('vrmkeff440_13', 4)

@State
def mk440cutin_Active2():

    def upon_IMMEDIATE():
        RenderLayer(2)
        PaletteIndex(2)
        AddY(-250000)
        Size(1400)

        def upon_33():
            sendToLabel(1)
    sprite('null', 8)
    CreateObject('mk440cutinEffStarEx2', -1)
    sprite('mk440cutin_05', 4)
    CreateObject('mk440cutinEffEx2', -1)
    IgnorePauses(3)
    physicsXImpulse(2000)
    physicsYImpulse(6000)
    sprite('mk440cutin_06', 2)
    physicsXImpulse(6000)
    physicsYImpulse(2000)
    sprite('mk440cutin_07', 3)
    physicsYImpulse(0)
    physicsXImpulse(10000)
    SetAcceleration(5000)
    sprite('mk440cutin_08', 30)
    physicsXImpulse(70000)
    SetAcceleration(10000)
    label(1)
    sprite('mk440cutin_09', 4)
    ConstantAlphaModifier(-31)
    EndMomentum(1)
    PassbackAddActionMarkToFunction('mk440cutinEffEx2', 32)
    sprite('mk440cutin_10', 4)

@State
def mk440cutinEffStarEx2():

    def upon_IMMEDIATE():
        RenderLayer(2)
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
    sprite('vrmkeff440_20', 2)
    sprite('vrmkeff440_21', 2)
    sprite('vrmkeff440_22', 2)
    sprite('vrmkeff440_23', 2)

@State
def mk440cutinEffEx2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        EnableAfterimage(1)
        AfterimageCount(2)
        sendToLabelUpon(32, 0)
        AlphaValue(255)
    sprite('vrmkeff440_24', 4)
    RenderLayer(2)
    sprite('vrmkeff440_25', 2)
    sprite('vrmkeff440_26', 3)
    sprite('vrmkeff440_28', 32767)
    label(0)
    sprite('vrmkeff440_29', 4)
    sprite('null', 1)
    CreateObject('mk440cutinEffEndEX2', -1)

@State
def mk440cutinEffEndEX2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(2)
        Size(1400)
    sprite('vrmkeff440_29', 2)
    sprite('vrmkeff440_30', 2)
    sprite('vrmkeff440_31', 2)
    sprite('vrmkeff440_32', 5)
    ConstantAlphaModifier(-51)

@State
def EntryMant2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
    sprite('vrmkef603m_00', 6)
    AddY(10000)
    sprite('vrmkef603m_01', 3)
    AddY(180000)
    sprite('vrmkef603m_01', 3)
    AddY(100000)

@State
def Event_mk430cutin_lv3():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        NoAttackDuringAction(1)
        PaletteIndex(1)
        BlendMode_Normal()
        Size(1000)
        AddX(45000)
        AddY(405000)
        if CharacterIDCheck('ta'):
            RenderLayer(1)
    sprite('null', 1)
    CreateObject('mkef_430bigpunch_lv3', -1)
    CreateObject('mk430effLv3', -1)
    sprite('mk430_punch00', 1)
    physicsXImpulse(100000)
    sprite('mk430_punch01', 1)
    AddX(30000)
    sprite('mk430_punch01', 1)
    AddX(35000)
    sprite('mk430_punchlv03', 1)
    AddX(60000)
    sprite('mk430_punchlv03', 4)
    physicsXImpulse(0)
    AddX(60000)
    sprite('mk430_punchlv03', 2)
    physicsXImpulse(-400)
    sprite('mk430_punchlv03', 8)
    physicsXImpulse(0)
    sprite('mk430_punchlv03', 15)
    StartMultihit()
    ConstantAlphaModifier(-15)
    BlendMode_Add()

@State
def Act3Event_Noel():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        XPositionRelativeFacing(-360000)
        SetZVal(750)
        EnableCollision(0)
        ScreenCollision(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(2, 1)
    sprite('no620_08', 32767)
    label(0)
    sprite('no064_02', 4)
    sprite('no064_03', 4)
    sprite('no064_04', 4)
    sprite('no064_05', 4)
    sprite('no064_06', 4)
    sprite('no064_07', 4)
    sprite('no064_08', 4)
    sprite('no033_00', 3)
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('no033_01', 3)
    physicsXImpulse(-26000)
    physicsYImpulse(12000)
    setGravity(800)
    JumpSoundEffects()
    JumpEffects(3, 100)
    label(9)
    sprite('no033_02', 2)
    sprite('no033_03', 2)
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('null', 2)
    EndMomentum(1)
    Visibility(1)

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